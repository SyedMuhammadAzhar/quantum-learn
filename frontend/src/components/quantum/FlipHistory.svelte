<script>
    import './flipHistory.css';
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
