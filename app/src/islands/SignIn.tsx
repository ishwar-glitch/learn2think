import { useEffect, useState } from 'react';
import { onAuthStateChanged, type User } from 'firebase/auth';
import { auth, isConfigured, signInWithGoogle, sendEmailLink, completeEmailLink, logOut } from '../lib/firebase';

export default function SignIn() {
  const [email, setEmail] = useState('');
  const [msg, setMsg] = useState('');
  const [user, setUser] = useState<User | null>(null);
  const ready = isConfigured();

  useEffect(() => onAuthStateChanged(auth, setUser), []);

  useEffect(() => {
    if (ready) completeEmailLink().catch((e) => setMsg('✕ ' + e.message));
  }, [ready]);

  const run = async (fn: () => Promise<unknown>, ok?: string) => {
    try { await fn(); if (ok) setMsg(ok); } catch (e) { setMsg('✕ ' + (e as Error).message); }
  };

  if (user) {
    return (
      <div className="max-w-sm space-y-4">
        <p role="status" className="border-l-4 border-willow bg-surface-2 p-3 text-sm">
          ✓ Signed in as {user.email ?? user.displayName}
        </p>
        <a href="/" className="inline-block rounded-full bg-accent px-5 py-3 font-semibold text-on-accent">Continue</a>
        <button onClick={() => logOut()} className="ml-3 rounded-full border border-line-strong px-5 py-3 font-medium">Sign out</button>
      </div>
    );
  }

  return (
    <div className="max-w-sm space-y-4">
      {!ready && (
        <p role="status" className="border-l-4 border-carrot bg-surface-2 p-3 text-sm">
          ✕ Sign-in is not connected yet. Firebase settings are placeholders.
        </p>
      )}
      <button disabled={!ready} onClick={() => run(signInWithGoogle)}
        className="w-full rounded-full border border-line-strong px-5 py-3 font-medium disabled:opacity-60">
        Continue with Google
      </button>
      <form onSubmit={(e) => { e.preventDefault(); run(() => sendEmailLink(email), 'Check your email for the sign-in link.'); }} className="space-y-2">
        <label htmlFor="email" className="text-sm font-medium">Email</label>
        <input id="email" type="email" required value={email} onChange={(e) => setEmail(e.target.value)}
          className="w-full rounded-lg border border-line-strong bg-surface px-3 py-2" />
        <button disabled={!ready} className="w-full rounded-full bg-accent px-5 py-3 font-semibold text-on-accent disabled:opacity-60">
          Email me a sign-in link
        </button>
      </form>
      {msg && <p role="status" className="text-sm">{msg}</p>}
    </div>
  );
}
