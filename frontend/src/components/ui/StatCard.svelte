<script>
    import './statCard.css';
    let { label = '', value = '', subtext = '' } = $props();
</script>

<div class="stat-card">
    <div class="stat-label">{label}</div>
    <div class="stat-value">{value}</div>
    {#if subtext}
        <div class="stat-subtext">{subtext}</div>
    {/if}
</div>
