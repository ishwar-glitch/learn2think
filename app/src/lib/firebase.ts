import { initializeApp, getApps } from 'firebase/app';
import { getAuth, GoogleAuthProvider, signInWithPopup, RecaptchaVerifier,
  signInWithPhoneNumber, signOut, type ConfirmationResult } from 'firebase/auth';
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

let verifier: RecaptchaVerifier | null = null;

// Sends an SMS code. `container` is the id of an empty element for the (invisible) reCAPTCHA check.
export async function sendPhoneCode(phone: string, container: string): Promise<ConfirmationResult> {
  verifier ??= new RecaptchaVerifier(auth, container, { size: 'invisible' });
  try {
    return await signInWithPhoneNumber(auth, phone, verifier);
  } catch (e) {
    verifier.clear();
    verifier = null;
    throw e;
  }
}

export const logOut = () => signOut(auth);
