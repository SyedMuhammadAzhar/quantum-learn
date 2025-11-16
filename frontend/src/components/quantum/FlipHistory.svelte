<script>
    let { history = [] } = $props();
</script>

{#if history.length > 0}
    <div class="history-container">
        <h4 class="history-title">Recent Results</h4>
        <div class="history-items">
            {#each history as result, index (index)}
                <span 
                    class="history-item" 
                    class:heads={result === 0}
                    class:tails={result === 1}
                    title={result === 0 ? 'Heads (|0⟩)' : 'Tails (|1⟩)'}
                >
                    {result === 0 ? 'H' : 'T'}
                </span>
            {/each}
        </div>
    </div>
{/if}

<style>
    .history-container {
        margin-top: var(--spacing-lg);
    }
    
    .history-title {
        margin: 0 0 var(--spacing-sm) 0;
        color: var(--color-text-primary);
        font-size: var(--font-size-base);
    }
    
    .history-items {
        display: flex;
        flex-wrap: wrap;
        gap: var(--spacing-xs);
    }
    
    .history-item {
        width: 28px;
        height: 28px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        color: white;
        font-size: var(--font-size-xs);
        transition: transform var(--transition-fast);
    }
    
    .history-item:hover {
        transform: scale(1.2);
    }
    
    .history-item.heads {
        background: var(--color-heads);
    }
    
    .history-item.tails {
        background: var(--color-tails);
    }
</style>