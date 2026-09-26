import { useState, type FormEvent } from 'react';
import { doc, setDoc, serverTimestamp } from 'firebase/firestore';
import { db, isConfigured } from '../lib/firebase';
import { track } from '../lib/telemetry';

const ROLES = ['BA', 'DA', 'PM', 'PD', 'Not sure'] as const;
type Status = 'idle' | 'sending' | 'done' | 'exists' | 'error';

async function sha256(s: string) {
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s));
  return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, '0')).join('');
}

const field = 'w-full rounded-lg border border-line-strong bg-surface px-3 py-2 text-ink';

export default function Waitlist() {
  const [status, setStatus] = useState<Status>('idle');
  const [err, setErr] = useState('');

  async function submit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const f = new FormData(e.currentTarget);
    if (f.get('website')) { setStatus('done'); return; } // honeypot: pretend success
    const email = String(f.get('email') ?? '').trim().toLowerCase();
    const role = String(f.get('role'));
    const learner = String(f.get('learner'));
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email) || email.length > 254) { setErr('Please enter a valid email address.'); return; }
    if (!isConfigured()) { setErr('The waitlist is not connected yet. Please try again soon.'); return; }
    setErr(''); setStatus('sending');
    try {
      await setDoc(doc(db, 'waitlist', await sha256(email)), { email, role, learner, createdAt: serverTimestamp() });
      track('waitlist_submitted', { role, learner_type: learner });
      setStatus('done');
    } catch (ex: any) {
      // A repeat signup is an update, which the rules deny.
      if (ex?.code === 'permission-denied') setStatus('exists');
      else { setStatus('error'); setErr('Something went wrong. Please try again.'); }
    }
  }

  if (status === 'done' || status === 'exists') {
    return (
      <p role="status" className="rounded-xl bg-ok-soft p-4 font-medium">
        {status === 'exists' ? 'You are already on the list. We will email you when the first case is ready.'
          : 'You are on the list. We will email you once, when the first case is ready, with your founding code.'}
      </p>
    );
  }
  return (
    <form onSubmit={submit} className="space-y-4" noValidate>
      <div>
        <label htmlFor="wl-email" className="mb-1 block font-medium">Email</label>
        <input id="wl-email" name="email" type="email" autoComplete="email" required maxLength={254} className={field} />
      </div>
      <div>
        <label htmlFor="wl-role" className="mb-1 block font-medium">I am aiming for</label>
        <select id="wl-role" name="role" defaultValue="Not sure" className={field}>
          {ROLES.map((r) => <option key={r}>{r}</option>)}
        </select>
      </div>
      <fieldset>
        <legend className="mb-1 font-medium">I am a</legend>
        <label className="mr-6 inline-flex items-center gap-2"><input type="radio" name="learner" value="student" defaultChecked /> Student</label>
        <label className="inline-flex items-center gap-2"><input type="radio" name="learner" value="switcher" /> Career switcher</label>
      </fieldset>
      <div aria-hidden="true" className="absolute -left-[9999px] h-0 w-0 overflow-hidden">
        <label>Website <input name="website" tabIndex={-1} autoComplete="off" /></label>
      </div>
      <p role="alert" className="min-h-[1.5rem] text-warn-line">{err}</p>
      <button disabled={status === 'sending'} className="rounded-full bg-accent px-6 py-3 font-semibold text-on-accent disabled:opacity-60">
        {status === 'sending' ? 'Joining…' : 'Join the waitlist'}
      </button>
    </form>
  );
}
