import { initializeApp, getApps } from 'firebase/app';
import { getAuth, GoogleAuthProvider, signInWithPopup, signOut } from 'firebase/auth';
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

export const logOut = () => signOut(auth);
