<script>
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

<style>
    .card {
        background: var(--color-surface);
        border-radius: var(--radius-lg);
        padding: var(--spacing-lg);
        box-shadow: var(--shadow-sm);
    }
    
    .card-info {
        background: #f0f8ff;
        border-left: 4px solid var(--color-secondary);
    }
    
    .card-success {
        background: #f0fff4;
        border-left: 4px solid var(--color-success);
    }
    
    .card-warning {
        background: #fffbf0;
        border-left: 4px solid var(--color-warning);
    }
    
    .card-title {
        margin: 0 0 var(--spacing-md) 0;
        color: var(--color-text-primary);
        font-size: var(--font-size-xl);
    }
    
    .card-content {
        color: var(--color-text-secondary);
    }
</style>