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
    border: 2px solid rgba(255, 255, 255, 0.3);
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    cursor: pointer;
    font-size: 1.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s ease;
    z-index: 1000;
  }

  .theme-toggle:hover {
    background: rgba(255, 255, 255, 0.2);
    transform: scale(1.1);
  }
</style>
