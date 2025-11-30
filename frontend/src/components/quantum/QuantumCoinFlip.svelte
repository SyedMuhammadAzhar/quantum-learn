<script>
  import "./quantumCoinFlip.css";
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
  let batchProgress = $state(0);

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
    batchProgress = 0;

    try {
      // Start the API call
      const batchPromise = quantumCoinApi.flipBatch(100);

      // Animate rapid flipping while waiting
      const animationDuration = 2000;
      const flipsToShow = 20;
      const flipInterval = animationDuration / flipsToShow;

      for (let i = 0; i < flipsToShow; i++) {
        batchProgress = Math.floor((i / flipsToShow) * 100);
        isSpinning = true;
        await new Promise((resolve) => setTimeout(resolve, flipInterval / 2));

        // Show random result briefly
        currentResult = Math.random() > 0.5 ? 1 : 0;
        stateLabel = currentResult === 0 ? "Heads" : "Tails";
        isSpinning = false;

        if (coinComponent) {
          await coinComponent.animateCollapse(currentResult);
        }
        await new Promise((resolve) => setTimeout(resolve, flipInterval / 2));
      }

      // Wait for API response
      const response = await batchPromise;

      coinFlipStore.addBatch(response.zeros, response.ones);
      stateLabel = `Batch: ${response.zeros}H / ${response.ones}T`;
      batchProgress = 100;

      // Show final dominant result
      currentResult = response.zeros > response.ones ? 0 : 1;
      isSpinning = false;
    } catch (error) {
      console.error("Batch flip failed:", error);
      errorMessage = error.message;
    } finally {
      isMeasuring = false;
      batchProgress = 0;
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
