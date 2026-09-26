import { readFileSync } from 'node:fs';
import { beforeAll, afterAll, beforeEach, describe, it } from 'vitest';
import { initializeTestEnvironment, assertSucceeds, assertFails } from '@firebase/rules-unit-testing';
import { doc, getDoc, setDoc, updateDoc, deleteDoc, serverTimestamp } from 'firebase/firestore';

let env;
const OWNED = ['profiles', 'plans', 'attempts', 'case_sessions', 'submissions',
  'thinking_records', 'stories', 'interview_attempts', 'rep_queue'];

beforeAll(async () => {
  env = await initializeTestEnvironment({
    projectId: 'demo-l2t',
    firestore: { rules: readFileSync(new URL('../firestore.rules', import.meta.url), 'utf8') },
  });
});
afterAll(() => env.cleanup());
beforeEach(() => env.clearFirestore());

const seed = (path, data) => env.withSecurityRulesDisabled((c) => setDoc(doc(c.firestore(), path), data));
const as = (uid) => env.authenticatedContext(uid).firestore();
const anon = () => env.unauthenticatedContext().firestore();

describe.each(OWNED)('%s (owner-only)', (col) => {
  it('owner can create, read, update, delete', async () => {
    const d = doc(as('alice'), `${col}/x`);
    await assertSucceeds(setDoc(d, { uid: 'alice', n: 1 }));
    await assertSucceeds(getDoc(d));
    await assertSucceeds(updateDoc(d, { n: 2 }));
    await assertSucceeds(deleteDoc(d));
  });
  it('other user cannot read, update or delete', async () => {
    await seed(`${col}/x`, { uid: 'alice' });
    const d = doc(as('bob'), `${col}/x`);
    await assertFails(getDoc(d));
    await assertFails(updateDoc(d, { n: 2 }));
    await assertFails(deleteDoc(d));
  });
  it('anonymous cannot read or write', async () => {
    await seed(`${col}/x`, { uid: 'alice' });
    await assertFails(getDoc(doc(anon(), `${col}/x`)));
    await assertFails(setDoc(doc(anon(), `${col}/y`), { uid: 'alice' }));
  });
  it('cannot create a document for someone else', async () => {
    await assertFails(setDoc(doc(as('bob'), `${col}/z`), { uid: 'alice' }));
  });
  it('owner cannot hand a document to another uid', async () => {
    await seed(`${col}/x`, { uid: 'alice' });
    await assertFails(updateDoc(doc(as('alice'), `${col}/x`), { uid: 'bob' }));
  });
});

describe('portfolio_items', () => {
  it('public items are readable by anyone, including signed-out', async () => {
    await seed('portfolio_items/p', { uid: 'alice', public: true });
    await assertSucceeds(getDoc(doc(anon(), 'portfolio_items/p')));
    await assertSucceeds(getDoc(doc(as('bob'), 'portfolio_items/p')));
  });
  it('private items are readable only by the owner', async () => {
    await seed('portfolio_items/p', { uid: 'alice', public: false });
    await assertSucceeds(getDoc(doc(as('alice'), 'portfolio_items/p')));
    await assertFails(getDoc(doc(as('bob'), 'portfolio_items/p')));
    await assertFails(getDoc(doc(anon(), 'portfolio_items/p')));
  });
  it('items without a public flag are private', async () => {
    await seed('portfolio_items/p', { uid: 'alice' });
    await assertFails(getDoc(doc(anon(), 'portfolio_items/p')));
  });
  it('only the owner can write, even if public', async () => {
    await seed('portfolio_items/p', { uid: 'alice', public: true });
    await assertFails(updateDoc(doc(as('bob'), 'portfolio_items/p'), { title: 'x' }));
    await assertFails(deleteDoc(doc(as('bob'), 'portfolio_items/p')));
    await assertSucceeds(updateDoc(doc(as('alice'), 'portfolio_items/p'), { title: 'x' }));
  });
});

describe('subscriptions and expert_reviews', () => {
  it('owner reads subscriptions but nobody writes from the client', async () => {
    await seed('subscriptions/s', { uid: 'alice', plan: 'plus' });
    await assertSucceeds(getDoc(doc(as('alice'), 'subscriptions/s')));
    await assertFails(getDoc(doc(as('bob'), 'subscriptions/s')));
    await assertFails(setDoc(doc(as('alice'), 'subscriptions/s2'), { uid: 'alice', plan: 'plus' }));
    await assertFails(updateDoc(doc(as('alice'), 'subscriptions/s'), { plan: 'pro' }));
  });
  it('owner can request a review but cannot change its outcome', async () => {
    await assertSucceeds(setDoc(doc(as('alice'), 'expert_reviews/r'), { uid: 'alice', status: 'requested' }));
    await assertFails(setDoc(doc(as('alice'), 'expert_reviews/r2'), { uid: 'alice', status: 'approved' }));
    await assertFails(updateDoc(doc(as('alice'), 'expert_reviews/r'), { status: 'approved' }));
    await assertFails(getDoc(doc(as('bob'), 'expert_reviews/r')));
  });
});

describe('unknown collections', () => {
  it('are locked', async () => {
    await assertFails(setDoc(doc(as('alice'), 'mystery/x'), { uid: 'alice' }));
    await assertFails(getDoc(doc(as('alice'), 'mystery/x')));
  });
});

describe('waitlist (create-only)', () => {
  const ID = 'a'.repeat(64);
  const good = () => ({ email: 'a@b.co', role: 'DA', learner: 'student', createdAt: serverTimestamp() });
  const at = (db, id = ID) => doc(db, `waitlist/${id}`);

  it('anonymous visitor can create a valid entry', () => assertSucceeds(setDoc(at(anon()), good())));
  it('second signup with same id is denied (dedupe)', async () => {
    await assertSucceeds(setDoc(at(anon()), good()));
    await assertFails(setDoc(at(anon()), good()));
  });
  it('denies read, update, delete', async () => {
    await seed(`waitlist/${ID}`, { email: 'a@b.co', role: 'DA', learner: 'student' });
    await assertFails(getDoc(at(anon())));
    await assertFails(getDoc(at(as('alice'))));
    await assertFails(updateDoc(at(anon()), { role: 'PM' }));
    await assertFails(deleteDoc(at(anon())));
  });
  it.each([
    ['bad email', { email: 'nope' }],
    ['long email', { email: 'a'.repeat(250) + '@b.co' }],
    ['bad role', { role: 'CEO' }],
    ['bad learner', { learner: 'x' }],
    ['extra field', { hp: 'bot' }],
    ['client timestamp', { createdAt: new Date() }],
  ])('rejects %s', (_n, patch) => assertFails(setDoc(at(anon()), { ...good(), ...patch })));
  it('rejects missing field', () => { const g = good(); delete g.role; return assertFails(setDoc(at(anon()), g)); });
  it('rejects a non-hash id', () => assertFails(setDoc(at(anon(), 'me@x.com'), good())));
});
