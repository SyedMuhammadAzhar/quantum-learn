<script>
  import './button.css';
  // @ts-nocheck

  let {
    variant = "primary",
    disabled = false,
    loading = false,
    size = "md",
    onclick = () => {},
    children,
  } = $props();

  let buttonClass = $derived(`btn btn-${variant} btn-${size}`);
</script>

<!-- svelte-ignore event_directive_deprecated -->
<button class={buttonClass} disabled={disabled || loading} on:click={onclick}>
  {#if loading}
    <span class="spinner"></span>
  {/if}
  {@render children()}
</button>
