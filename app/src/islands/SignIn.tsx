import { useEffect, useState } from 'react';
import { onAuthStateChanged, type ConfirmationResult, type User } from 'firebase/auth';
import { auth, isConfigured, signInWithGoogle, sendPhoneCode, logOut } from '../lib/firebase';

export default function SignIn() {
  const [phone, setPhone] = useState('+91');
  const [code, setCode] = useState('');
  const [pending, setPending] = useState<ConfirmationResult | null>(null);
  const [msg, setMsg] = useState('');
  const [user, setUser] = useState<User | null>(null);
  const ready = isConfigured();

  useEffect(() => onAuthStateChanged(auth, setUser), []);

  const run = async (fn: () => Promise<unknown>, ok?: string) => {
    try { await fn(); if (ok) setMsg(ok); } catch (e) { setMsg('✕ ' + (e as Error).message); }
  };

  if (user) {
    return (
      <div className="max-w-sm space-y-4">
        <p role="status" className="border-l-4 border-willow bg-surface-2 p-3 text-sm">
          ✓ Signed in as {user.email ?? user.phoneNumber ?? user.displayName}
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
      {!pending ? (
        <form onSubmit={(e) => { e.preventDefault(); run(async () => setPending(await sendPhoneCode(phone.replace(/\s/g, ''), 'recaptcha-box')), 'We sent a code by SMS.'); }} className="space-y-2">
          <label htmlFor="phone" className="text-sm font-medium">Mobile number (with country code)</label>
          <input id="phone" type="tel" inputMode="tel" autoComplete="tel" required value={phone} onChange={(e) => setPhone(e.target.value)}
            className="w-full rounded-lg border border-line-strong bg-surface px-3 py-2" />
          <button disabled={!ready} className="w-full rounded-full bg-accent px-5 py-3 font-semibold text-on-accent disabled:opacity-60">
            Send code
          </button>
        </form>
      ) : (
        <form onSubmit={(e) => { e.preventDefault(); run(() => pending.confirm(code.trim())); }} className="space-y-2">
          <label htmlFor="code" className="text-sm font-medium">6-digit code</label>
          <input id="code" inputMode="numeric" autoComplete="one-time-code" required value={code} onChange={(e) => setCode(e.target.value)}
            className="w-full rounded-lg border border-line-strong bg-surface px-3 py-2" />
          <button className="w-full rounded-full bg-accent px-5 py-3 font-semibold text-on-accent">Verify</button>
          <button type="button" onClick={() => { setPending(null); setCode(''); setMsg(''); }} className="text-sm underline">Use a different number</button>
        </form>
      )}
      <div id="recaptcha-box" />
      {msg && <p role="status" className="text-sm">{msg}</p>}
    </div>
  );
}
