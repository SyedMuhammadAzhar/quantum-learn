<script>
    let { 
        value = 0, 
        label = '', 
        color = 'primary', 
        showValue = true, 
        animated = true 
    } = $props();
</script>

<div class="progress-container">
    {#if label}
        <div class="progress-label">{label}</div>
    {/if}
    <div class="progress-bar">
        <div 
            class="progress-fill progress-{color}" 
            class:animated
            style="width: {value}%"
        ></div>
    </div>
    {#if showValue}
        <div class="progress-value">{value}%</div>
    {/if}
</div>

<style>
    .progress-container {
        display: flex;
        align-items: center;
        gap: var(--spacing-sm);
    }
    
    .progress-label {
        width: 60px;
        font-weight: 600;
        color: var(--color-text-primary);
        font-size: var(--font-size-sm);
    }
    
    .progress-bar {
        flex: 1;
        height: 24px;
        background: var(--color-border);
        border-radius: var(--radius-full);
        overflow: hidden;
    }
    
    .progress-fill {
        height: 100%;
        border-radius: var(--radius-full);
        transition: width var(--transition-slow);
    }
    
    .progress-fill.animated {
        transition: width 0.8s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .progress-value {
        width: 55px;
        font-weight: 700;
        color: var(--color-text-primary);
        font-size: var(--font-size-sm);
        text-align: right;
    }
    
    /* Color variants */
    .progress-primary {
        background: linear-gradient(90deg, var(--color-primary), var(--color-primary-dark));
    }
    
    .progress-heads {
        background: linear-gradient(90deg, var(--color-heads), var(--color-heads-light));
    }
    
    .progress-tails {
        background: linear-gradient(90deg, var(--color-tails), var(--color-tails-light));
    }
    
    .progress-success {
        background: linear-gradient(90deg, var(--color-success), #2ecc71);
    }
    
    .progress-info {
        background: linear-gradient(90deg, var(--color-info), #5dade2);
    }
</style>