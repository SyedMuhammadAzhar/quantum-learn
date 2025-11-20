<script>
    import './card.css';
    let { title = '', variant = 'default', children } = $props();
</script>

<div class="card card-{variant}">
    {#if title}
        <h3 class="card-title">{title}</h3>
    {/if}
    <div class="card-content">
        {@render children()}
    </div>
</div>
