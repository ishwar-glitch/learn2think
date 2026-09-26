import { initializeApp, getApps } from 'firebase/app';
import { getAuth, GoogleAuthProvider, signInWithPopup, sendSignInLinkToEmail,
  isSignInWithEmailLink, signInWithEmailLink, signOut } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';

// Placeholder config from .env (see .env.example). No Firebase project exists yet.
const env = import.meta.env;
const config = {
  apiKey: env.PUBLIC_FIREBASE_API_KEY ?? 'placeholder',
  authDomain: env.PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: env.PUBLIC_FIREBASE_PROJECT_ID ?? 'placeholder',
  storageBucket: env.PUBLIC_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: env.PUBLIC_FIREBASE_MESSAGING_SENDER_ID,
  appId: env.PUBLIC_FIREBASE_APP_ID,
};

export const isConfigured = () => !!config.apiKey && config.apiKey !== 'placeholder';
const app = getApps()[0] ?? initializeApp(config);
export const auth = getAuth(app);
export const db = getFirestore(app);

export const signInWithGoogle = () => signInWithPopup(auth, new GoogleAuthProvider());

export async function sendEmailLink(email: string) {
  await sendSignInLinkToEmail(auth, email, { url: `${location.origin}/signin`, handleCodeInApp: true });
  localStorage.setItem('l2t-email', email);
}

export async function completeEmailLink() {
  if (!isSignInWithEmailLink(auth, location.href)) return null;
  const email = localStorage.getItem('l2t-email') ?? window.prompt('Confirm your email to finish signing in');
  if (!email) return null;
  const cred = await signInWithEmailLink(auth, email, location.href);
  localStorage.removeItem('l2t-email');
  return cred.user;
}

export const logOut = () => signOut(auth);
