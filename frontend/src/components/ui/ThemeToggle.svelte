<script>
  import { theme, toggleTheme } from '../../stores/themeStore.js';
</script>

<button class="theme-toggle" onclick={toggleTheme} aria-label="Toggle theme">
  {#if $theme === 'light'}
    🌙
  {:else}
    ☀️
  {/if}
</button>

<style>
  .theme-toggle {
    position: fixed;
    top: 1.5rem;
    right: 1.5rem;
    width: 3rem;
    height: 3rem;
    border-radius: 50%;
    border: 2px solid rgba(255, 255, 255, 0.5);
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(10px);
    cursor: pointer;
    font-size: 1.5rem;
    display: flex !important;
    align-items: center;
    justify-content: center;
    transition: all 0.3s ease;
    z-index: 99999;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    opacity: 1 !important;
    visibility: visible !important;
    pointer-events: auto !important;
  }

  [data-theme="dark"] .theme-toggle {
    border-color: rgba(255, 255, 255, 0.4);
    background: rgba(30, 41, 59, 0.8);
  }

  .theme-toggle:hover {
    background: rgba(255, 255, 255, 0.3);
    transform: scale(1.1);
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.4);
  }

  [data-theme="dark"] .theme-toggle:hover {
    background: rgba(30, 41, 59, 0.9);
  }
</style>
