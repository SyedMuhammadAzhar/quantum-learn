<script>
    import './progressBar.css';
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
