import { writable } from 'svelte/store';

const stored = typeof window !== 'undefined' ? localStorage.getItem('theme') : null;
export const theme = writable(stored || 'light');

theme.subscribe(value => {
  if (typeof window !== 'undefined') {
    localStorage.setItem('theme', value);
    document.documentElement.setAttribute('data-theme', value);
  }
});

export function toggleTheme() {
  theme.update(current => current === 'light' ? 'dark' : 'light');
}
