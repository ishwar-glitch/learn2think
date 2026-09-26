import { useEffect, useState } from 'react';

export default function ThemeToggle() {
  const [dark, setDark] = useState(false);
  useEffect(() => setDark(document.documentElement.dataset.theme === 'dark'), []);
  const flip = () => {
    const next = dark ? 'light' : 'dark';
    document.documentElement.dataset.theme = next;
    try { localStorage.setItem('l2t-theme', next); } catch {}
    setDark(!dark);
  };
  return (
    <button onClick={flip} aria-pressed={dark}
      className="rounded-full border border-line-strong px-4 py-1.5 text-sm">
      {dark ? 'Light mode' : 'Dark mode'}
    </button>
  );
}
