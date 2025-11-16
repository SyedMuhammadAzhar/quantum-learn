<script>
  // @ts-nocheck

  import { onMount } from "svelte";
  import { quantumCoinApi } from "../../services/api.js";
  import {
    coinFlipStore,
    coinFlipPercentages,
  } from "../../stores/coinFlipStore.js";

  import Button from "../ui/Button.svelte";
  import Card from "../ui/Card.svelte";
  import StatCard from "../ui/StatCard.svelte";
  import ProgressBar from "../ui/ProgressBar.svelte";
  import Coin from "./Coin.svelte";
  import FlipHistory from "./FlipHistory.svelte";

  let coinComponent = $state(null);
  let isSpinning = $state(true);
  let isMeasuring = $state(false);
  let currentResult = $state(null);
  let stateLabel = $state("Superposition");
  let errorMessage = $state("");

  async function measure() {
    if (isMeasuring) return;

    isMeasuring = true;
    errorMessage = "";

    try {
      const response = await quantumCoinApi.flipOnce();

      if (coinComponent) {
        await coinComponent.animateCollapse(response.result);
      }

      currentResult = response.result;
      stateLabel = response.result_label;
      isSpinning = false;

      coinFlipStore.addFlip(response.result);
    } catch (error) {
      console.error("Measurement failed:", error);
      errorMessage = error.message;
      stateLabel = "Error";
    } finally {
      isMeasuring = false;
    }
  }

  async function prepareSuperposition() {
    if (isMeasuring) return;

    if (coinComponent) {
      await coinComponent.resetPosition();
    }
    isSpinning = true;
    currentResult = null;
    stateLabel = "Superposition";
  }

  async function runBatch() {
    if (isMeasuring) return;

    isMeasuring = true;
    errorMessage = "";

    try {
      const batchPromise = quantumCoinApi.flipBatch(100);
      const animPromise = coinComponent
        ? coinComponent.animateBatch()
        : Promise.resolve();

      const [response] = await Promise.all([batchPromise, animPromise]);

      coinFlipStore.addBatch(response.zeros, response.ones);
      stateLabel = `Batch: ${response.zeros}H / ${response.ones}T`;
    } catch (error) {
      console.error("Batch flip failed:", error);
      errorMessage = error.message;
    } finally {
      isMeasuring = false;
    }
  }

  function clearStatistics() {
    coinFlipStore.reset();
  }
</script>

<div class="quantum-coin-flip">
  <!-- Educational Explanation -->
  <Card variant="info">
    <h2 class="section-title">Quantum Coin Flip</h2>
    {#if isSpinning}
      <p>
        The coin is in <strong>superposition</strong> — it exists as both heads
        AND tails simultaneously! This quantum state is created by applying a
        <strong>Hadamard gate</strong> to a qubit, transforming |0⟩ into (|0⟩ + |1⟩)/√2.
      </p>
    {:else if currentResult !== null}
      <p>
        The measurement caused <strong>wave function collapse</strong>! The
        superposition collapsed to a definite state:
        <strong>{stateLabel}</strong>. Each measurement has exactly 50%
        probability for heads or tails.
      </p>
    {:else}
      <p>
        Click "Prepare Superposition" to put the quantum coin into a
        superposition state, then measure it to observe the collapse.
      </p>
    {/if}
  </Card>

  <!-- Error Display -->
  {#if errorMessage}
    <Card variant="warning">
      <p><strong>Error:</strong> {errorMessage}</p>
    </Card>
  {/if}

  <!-- Coin Visualization -->
  <div class="coin-section">
    <Coin bind:this={coinComponent} {isSpinning} result={currentResult} />
    <div class="state-label">{stateLabel}</div>
  </div>

  <!-- Controls -->
  <div class="controls">
    {#if isSpinning}
      <Button
        variant="danger"
        size="lg"
        onclick={measure}
        loading={isMeasuring}
        disabled={isMeasuring}
      >
        🔬 Measure
      </Button>
    {:else}
      <Button variant="success" size="lg" onclick={prepareSuperposition}>
        🔄 Prepare Superposition
      </Button>
    {/if}

    <Button
      variant="purple"
      size="lg"
      onclick={runBatch}
      loading={isMeasuring}
      disabled={isMeasuring}
    >
      ⚡ Run 100 Flips
    </Button>
  </div>

  <!-- Statistics -->
  <Card title="Statistics">
    <div class="stats-grid">
      <StatCard label="Total Flips" value={$coinFlipStore.totalFlips} />
      <StatCard
        label="Heads (|0⟩)"
        value={$coinFlipStore.headsCount}
        subtext="{$coinFlipPercentages.headsFormatted}%"
      />
      <StatCard
        label="Tails (|1⟩)"
        value={$coinFlipStore.tailsCount}
        subtext="{$coinFlipPercentages.tailsFormatted}%"
      />
    </div>

    <div class="probability-section">
      <ProgressBar
        label="Heads"
        value={$coinFlipPercentages.heads}
        color="heads"
      />
      <ProgressBar
        label="Tails"
        value={$coinFlipPercentages.tails}
        color="tails"
      />
      <p class="theoretical-note">
        <small
          >Theoretical probability: 50% each (Hadamard gate creates equal
          superposition)</small
        >
      </p>
    </div>

    <FlipHistory history={$coinFlipStore.history} />

    <div class="clear-section">
      <Button variant="secondary" size="sm" onclick={clearStatistics}>
        Clear Statistics
      </Button>
    </div>
  </Card>
</div>

<style>
  .quantum-coin-flip {
    display: flex;
    flex-direction: column;
    gap: var(--spacing-lg);
  }

  .section-title {
    margin-top: 0;
    color: var(--color-text-primary);
  }

  .coin-section {
    display: flex;
    flex-direction: column;
    align-items: center;
    background: var(--color-surface);
    border-radius: var(--radius-lg);
    padding: var(--spacing-lg);
    box-shadow: var(--shadow-sm);
  }

  .state-label {
    font-size: var(--font-size-2xl);
    font-weight: 700;
    color: var(--color-text-primary);
    margin-top: var(--spacing-md);
  }

  .controls {
    display: flex;
    gap: var(--spacing-md);
    justify-content: center;
    flex-wrap: wrap;
  }

  .stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: var(--spacing-md);
    margin-bottom: var(--spacing-lg);
  }

  .probability-section {
    display: flex;
    flex-direction: column;
    gap: var(--spacing-sm);
  }

  .theoretical-note {
    text-align: center;
    color: var(--color-text-muted);
    margin-top: var(--spacing-sm);
  }

  .clear-section {
    margin-top: var(--spacing-lg);
    text-align: center;
  }
</style>
