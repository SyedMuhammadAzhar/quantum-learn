<script>
  import { quantumCoinApi, doubleCoinApi } from "../../services/api.js";
  import Button from "../ui/Button.svelte";
  import Card from "../ui/Card.svelte";
  import ProgressBar from "../ui/ProgressBar.svelte";
  import StatCard from "../ui/StatCard.svelte";

  // Mode: 'single' or 'double'
  let mode = $state("single");

  // Single coin state
  let singleResult = $state(null);
  let singleStats = $state({ total: 0, heads: 0, tails: 0 });
  let singleHistory = $state([]);

  // Double coin state
  let doubleResult = $state(null);
  let doubleStats = $state({
    total: 0,
    counts: { "00": 0, "01": 0, "10": 0, "11": 0 },
  });
  let doubleHistory = $state([]);

  // Shared state
  let isSpinning = $state(true);
  let isMeasuring = $state(false);
  let errorMessage = $state("");
  let isAnimatingBatch = $state(false);
  let batchFlipCount = $state(0);

  // Derived: Single coin percentages
  let singlePercentages = $derived({
    heads:
      singleStats.total > 0
        ? ((singleStats.heads / singleStats.total) * 100).toFixed(1)
        : "0.0",
    tails:
      singleStats.total > 0
        ? ((singleStats.tails / singleStats.total) * 100).toFixed(1)
        : "0.0",
  });

  // Derived: Double coin percentages
  let doublePercentages = $derived({
    "00":
      doubleStats.total > 0
        ? ((doubleStats.counts["00"] / doubleStats.total) * 100).toFixed(1)
        : "0.0",
    "01":
      doubleStats.total > 0
        ? ((doubleStats.counts["01"] / doubleStats.total) * 100).toFixed(1)
        : "0.0",
    "10":
      doubleStats.total > 0
        ? ((doubleStats.counts["10"] / doubleStats.total) * 100).toFixed(1)
        : "0.0",
    "11":
      doubleStats.total > 0
        ? ((doubleStats.counts["11"] / doubleStats.total) * 100).toFixed(1)
        : "0.0",
  });

  function switchMode(newMode) {
    mode = newMode;
    isSpinning = true;
    singleResult = null;
    doubleResult = null;
    errorMessage = "";
  }

  function clearAllStats() {
    singleStats = { total: 0, heads: 0, tails: 0 };
    singleHistory = [];
    doubleStats = { total: 0, counts: { "00": 0, "01": 0, "10": 0, "11": 0 } };
    doubleHistory = [];
  }

  async function measure() {
    if (isMeasuring) return;
    isMeasuring = true;
    errorMessage = "";

    try {
      if (mode === "single") {
        const response = await quantumCoinApi.flipOnce();
        singleResult = response;
        singleStats.total++;
        if (response.result === 0) {
          singleStats.heads++;
        } else {
          singleStats.tails++;
        }
        singleHistory = [...singleHistory, response.result].slice(-30);
      } else {
        const response = await doubleCoinApi.flipOnce();
        doubleResult = response;
        doubleStats.total++;
        const key = `${response.coin1}${response.coin2}`;
        doubleStats.counts[key]++;
        doubleHistory = [...doubleHistory, key].slice(-20);
      }
      isSpinning = false;
    } catch (error) {
      errorMessage = error.message;
    } finally {
      isMeasuring = false;
    }
  }

  async function runBatch() {
    if (isMeasuring) return;
    isMeasuring = true;
    isAnimatingBatch = true;
    errorMessage = "";

    try {
      // Animate rapid flipping for visual effect
      const totalFlips = 100;
      const animationDuration = 2000; // 2 seconds total
      const flipInterval = animationDuration / 20; // Show ~20 rapid flips

      // Start rapid flip animation
      for (let i = 0; i < 20; i++) {
        batchFlipCount = Math.floor((i / 20) * totalFlips);
        isSpinning = true;
        await new Promise((resolve) => setTimeout(resolve, flipInterval / 2));

        // Show random result briefly
        if (mode === "single") {
          singleResult = {
            result: Math.random() > 0.5 ? 1 : 0,
            result_label: Math.random() > 0.5 ? "Tails" : "Heads",
          };
        } else {
          const coin1 = Math.random() > 0.5 ? 1 : 0;
          const coin2 = Math.random() > 0.5 ? 1 : 0;
          doubleResult = {
            coin1,
            coin2,
            coin1_label: coin1 === 0 ? "Heads" : "Tails",
            coin2_label: coin2 === 0 ? "Heads" : "Tails",
          };
        }
        isSpinning = false;
        await new Promise((resolve) => setTimeout(resolve, flipInterval / 2));
      }

      // Now do the actual API call
      if (mode === "single") {
        const response = await quantumCoinApi.flipBatch(100);
        singleStats.total += response.total_shots;
        singleStats.heads += response.zeros;
        singleStats.tails += response.ones;
        // Show final state
        singleResult = {
          result: response.zeros > response.ones ? 0 : 1,
          result_label: response.zeros > response.ones ? "Heads" : "Tails",
        };
      } else {
        const response = await doubleCoinApi.flipBatch(100);
        doubleStats.total += response.total_shots;
        doubleStats.counts["00"] += response.counts["00"];
        doubleStats.counts["01"] += response.counts["01"];
        doubleStats.counts["10"] += response.counts["10"];
        doubleStats.counts["11"] += response.counts["11"];
        // Show the most frequent result
        const maxKey = Object.entries(response.counts).reduce((a, b) =>
          a[1] > b[1] ? a : b
        )[0];
        doubleResult = {
          coin1: parseInt(maxKey[0]),
          coin2: parseInt(maxKey[1]),
          coin1_label: maxKey[0] === "0" ? "Heads" : "Tails",
          coin2_label: maxKey[1] === "0" ? "Heads" : "Tails",
        };
      }
      batchFlipCount = totalFlips;
    } catch (error) {
      errorMessage = error.message;
    } finally {
      isMeasuring = false;
      isAnimatingBatch = false;
      isSpinning = false;
    }
  }

  function prepareSuperposition() {
    isSpinning = true;
    singleResult = null;
    doubleResult = null;
  }

  // Helper to get outcome label
  function getOutcomeLabel(key) {
    const labels = {
      "00": "Both Heads",
      "01": "H & T",
      "10": "T & H",
      "11": "Both Tails",
    };
    return labels[key] || key;
  }

  // Helper to get outcome emoji
  function getOutcomeEmoji(key) {
    const emojis = {
      "00": "🟡🟡",
      "01": "🟡🔵",
      "10": "🔵🟡",
      "11": "🔵🔵",
    };
    return emojis[key] || key;
  }
</script>

<div class="quantum-demo">
  <!-- Mode Selector Tabs -->
  <div class="mode-tabs">
    <button
      class="mode-tab"
      class:active={mode === "single"}
      onclick={() => switchMode("single")}
    >
      <span class="tab-icon">🪙</span>
      <span class="tab-content">
        <span class="tab-title">Single Coin</span>
        <span class="tab-subtitle">1 Qubit • 2 States • 50% each</span>
      </span>
    </button>

    <button
      class="mode-tab"
      class:active={mode === "double"}
      onclick={() => switchMode("double")}
    >
      <span class="tab-icon">🪙🪙</span>
      <span class="tab-content">
        <span class="tab-title">Double Coin</span>
        <span class="tab-subtitle">2 Qubits • 4 States • 25% each</span>
      </span>
    </button>
  </div>

  <!-- Circuit Explanation -->
  <div class="circuit-card">
    {#if mode === "single"}
      <div class="circuit-header">
        <h3>⚛️ Single Qubit Circuit</h3>
      </div>
      <div class="circuit-content">
        <div class="circuit-diagram">
          <div class="circuit-line">
            <span class="qubit-label">|0⟩</span>
            <span class="wire">───</span>
            <span class="gate hadamard">H</span>
            <span class="wire">───</span>
            <span class="measure">📏</span>
            <span class="wire">───</span>
            <span class="output">0 or 1</span>
          </div>
        </div>
        <p class="circuit-explain">
          The <strong>Hadamard gate (H)</strong> transforms |0⟩ into equal
          superposition:
          <code>(|0⟩ + |1⟩) / √2</code>
        </p>
      </div>
    {:else}
      <div class="circuit-header">
        <h3>⚛️ Two Qubit Circuit</h3>
      </div>
      <div class="circuit-content">
        <div class="circuit-diagram">
          <div class="circuit-line">
            <span class="qubit-label">|0⟩</span>
            <span class="wire">───</span>
            <span class="gate hadamard">H</span>
            <span class="wire">───</span>
            <span class="measure">📏</span>
            <span class="wire">─┐</span>
          </div>
          <div class="circuit-line">
            <span class="qubit-label">|0⟩</span>
            <span class="wire">───</span>
            <span class="gate hadamard">H</span>
            <span class="wire">───</span>
            <span class="measure">📏</span>
            <span class="wire">─┘</span>
            <span class="output">→ 00, 01, 10, 11</span>
          </div>
        </div>
        <p class="circuit-explain">
          <strong>Two independent Hadamard gates</strong> create 4-state
          superposition:
          <code>(|00⟩ + |01⟩ + |10⟩ + |11⟩) / 2</code>
        </p>
      </div>
    {/if}
  </div>

  <!-- Error Display -->
  {#if errorMessage}
    <div class="error-box">
      <span class="error-icon">⚠️</span>
      <p>{errorMessage}</p>
    </div>
  {/if}

  <!-- Coin Display Area -->
  <div class="coin-display-area">
    {#if mode === "single"}
      <!-- Single Coin -->
      <div class="single-coin-container">
        <div
          class="coin-wrapper-3d"
          class:spinning={isSpinning}
          class:batch-spinning={isAnimatingBatch}
        >
          <div
            class="coin-3d"
            class:measured={!isSpinning && singleResult}
            class:show-tails={!isSpinning &&
              singleResult &&
              singleResult.result === 1}
          >
            <!-- Heads side (front) -->
            <div class="coin-side coin-heads">
              <span class="coin-letter">H</span>
            </div>
            <!-- Tails side (back) -->
            <div class="coin-side coin-tails">
              <span class="coin-letter">T</span>
            </div>
          </div>
        </div>

        <div class="state-label">
          {#if isAnimatingBatch}
            <span class="state-text batch-text"
              >Running {batchFlipCount}/100 measurements...</span
            >
            <span class="state-description">Watch the quantum randomness!</span>
          {:else if isSpinning}
            <span class="state-text superposition-text"
              >|ψ⟩ = (|0⟩ + |1⟩) / √2</span
            >
            <span class="state-description"
              >Superposition - Both states at once!</span
            >
          {:else if singleResult}
            <span class="state-text measured-text"
              >|{singleResult.result}⟩ = {singleResult.result === 0
                ? "HEADS"
                : "TAILS"}</span
            >
            <span class="state-description">Collapsed to definite state</span>
          {/if}
        </div>
      </div>
    {:else}
      <!-- Double Coins -->
      <div class="double-coin-container">
        <div class="coin-pair">
          <!-- Coin 1 -->
          <div class="coin-unit">
            <div
              class="coin-wrapper-3d"
              class:spinning={isSpinning}
              class:batch-spinning={isAnimatingBatch}
            >
              <div
                class="coin-3d"
                class:measured={!isSpinning && doubleResult}
                class:show-tails={!isSpinning &&
                  doubleResult &&
                  doubleResult.coin1 === 1}
              >
                <div class="coin-side coin-heads">
                  <span class="coin-letter">H</span>
                </div>
                <div class="coin-side coin-tails">
                  <span class="coin-letter">T</span>
                </div>
              </div>
            </div>
            <span class="coin-name">Qubit 1</span>
          </div>

          <div class="coin-separator">
            <span class="tensor">⊗</span>
          </div>

          <!-- Coin 2 -->
          <div class="coin-unit">
            <div
              class="coin-wrapper-3d"
              class:spinning={isSpinning}
              class:batch-spinning={isAnimatingBatch}
              style="animation-delay: 0.15s"
            >
              <div
                class="coin-3d"
                class:measured={!isSpinning && doubleResult}
                class:show-tails={!isSpinning &&
                  doubleResult &&
                  doubleResult.coin2 === 1}
              >
                <div class="coin-side coin-heads">
                  <span class="coin-letter">H</span>
                </div>
                <div class="coin-side coin-tails">
                  <span class="coin-letter">T</span>
                </div>
              </div>
            </div>
            <span class="coin-name">Qubit 2</span>
          </div>
        </div>

        <div class="state-label">
          {#if isAnimatingBatch}
            <span class="state-text batch-text"
              >Running {batchFlipCount}/100 measurements...</span
            >
            <span class="state-description">Watch the quantum randomness!</span>
          {:else if isSpinning}
            <span class="state-text superposition-text"
              >|ψ⟩ = (|00⟩ + |01⟩ + |10⟩ + |11⟩) / 2</span
            >
            <span class="state-description">4-state superposition!</span>
          {:else if doubleResult}
            <span class="state-text measured-text"
              >|{doubleResult.coin1}{doubleResult.coin2}⟩ = {doubleResult.coin1 ===
              0
                ? "Heads"
                : "Tails"}
              & {doubleResult.coin2 === 0 ? "Heads" : "Tails"}</span
            >
            <span class="state-description">Collapsed to one of 4 states</span>
          {/if}
        </div>
      </div>
    {/if}
  </div>

  <!-- Control Buttons -->
  <div class="control-buttons">
    {#if isSpinning && !isAnimatingBatch}
      <Button
        variant="danger"
        size="lg"
        onclick={measure}
        loading={isMeasuring}
        disabled={isMeasuring}
      >
        🔬 Measure (Collapse!)
      </Button>
    {:else if isAnimatingBatch}
      <Button variant="secondary" size="lg" disabled={true}>
        ⏳ Running measurements...
      </Button>
    {:else}
      <Button variant="success" size="lg" onclick={prepareSuperposition}>
        🔄 Reset to Superposition
      </Button>
    {/if}

    <Button
      variant="purple"
      size="lg"
      onclick={runBatch}
      loading={isMeasuring}
      disabled={isMeasuring}
    >
      ⚡ Run 100 Measurements
    </Button>
  </div>

  <!-- Statistics Section -->
  <div class="stats-section">
    <div class="stats-header">
      <h3>📊 Statistics</h3>
      <button class="clear-btn" onclick={clearAllStats}>Clear All</button>
    </div>

    {#if mode === "single"}
      <!-- Single Coin Stats -->
      <div class="stats-content">
        <div class="stat-cards-row">
          <div class="stat-card total">
            <span class="stat-value">{singleStats.total}</span>
            <span class="stat-label">Total Flips</span>
          </div>
          <div class="stat-card heads">
            <span class="stat-value">{singleStats.heads}</span>
            <span class="stat-label">Heads |0⟩</span>
            <span class="stat-percent">{singlePercentages.heads}%</span>
          </div>
          <div class="stat-card tails">
            <span class="stat-value">{singleStats.tails}</span>
            <span class="stat-label">Tails |1⟩</span>
            <span class="stat-percent">{singlePercentages.tails}%</span>
          </div>
        </div>

        <div class="progress-bars">
          <div class="progress-item">
            <span class="progress-label">Heads</span>
            <div class="progress-track">
              <div
                class="progress-fill heads"
                style="width: {singlePercentages.heads}%"
              ></div>
            </div>
            <span class="progress-value">{singlePercentages.heads}%</span>
          </div>
          <div class="progress-item">
            <span class="progress-label">Tails</span>
            <div class="progress-track">
              <div
                class="progress-fill tails"
                style="width: {singlePercentages.tails}%"
              ></div>
            </div>
            <span class="progress-value">{singlePercentages.tails}%</span>
          </div>
        </div>

        <p class="theory-text">📐 Theoretical probability: 50% each</p>

        {#if singleHistory.length > 0}
          <div class="history-section">
            <h4>Recent Results</h4>
            <div class="history-dots">
              {#each singleHistory as result, i}
                <span
                  class="dot"
                  class:heads={result === 0}
                  class:tails={result === 1}
                  style="animation-delay: {i * 0.02}s"
                >
                  {result === 0 ? "H" : "T"}
                </span>
              {/each}
            </div>
          </div>
        {/if}
      </div>
    {:else}
      <!-- Double Coin Stats -->
      <div class="stats-content">
        <div class="stat-cards-row four">
          <div class="stat-card outcome-00">
            <span class="stat-emoji">🟡🟡</span>
            <span class="stat-value">{doubleStats.counts["00"]}</span>
            <span class="stat-label">|00⟩ Both H</span>
            <span class="stat-percent">{doublePercentages["00"]}%</span>
          </div>
          <div class="stat-card outcome-01">
            <span class="stat-emoji">🟡🔵</span>
            <span class="stat-value">{doubleStats.counts["01"]}</span>
            <span class="stat-label">|01⟩ H & T</span>
            <span class="stat-percent">{doublePercentages["01"]}%</span>
          </div>
          <div class="stat-card outcome-10">
            <span class="stat-emoji">🔵🟡</span>
            <span class="stat-value">{doubleStats.counts["10"]}</span>
            <span class="stat-label">|10⟩ T & H</span>
            <span class="stat-percent">{doublePercentages["10"]}%</span>
          </div>
          <div class="stat-card outcome-11">
            <span class="stat-emoji">🔵🔵</span>
            <span class="stat-value">{doubleStats.counts["11"]}</span>
            <span class="stat-label">|11⟩ Both T</span>
            <span class="stat-percent">{doublePercentages["11"]}%</span>
          </div>
        </div>

        <div class="progress-bars">
          <div class="progress-item">
            <span class="progress-label">|00⟩</span>
            <div class="progress-track">
              <div
                class="progress-fill outcome-00"
                style="width: {doublePercentages['00']}%"
              ></div>
            </div>
            <span class="progress-value">{doublePercentages["00"]}%</span>
          </div>
          <div class="progress-item">
            <span class="progress-label">|01⟩</span>
            <div class="progress-track">
              <div
                class="progress-fill outcome-01"
                style="width: {doublePercentages['01']}%"
              ></div>
            </div>
            <span class="progress-value">{doublePercentages["01"]}%</span>
          </div>
          <div class="progress-item">
            <span class="progress-label">|10⟩</span>
            <div class="progress-track">
              <div
                class="progress-fill outcome-10"
                style="width: {doublePercentages['10']}%"
              ></div>
            </div>
            <span class="progress-value">{doublePercentages["10"]}%</span>
          </div>
          <div class="progress-item">
            <span class="progress-label">|11⟩</span>
            <div class="progress-track">
              <div
                class="progress-fill outcome-11"
                style="width: {doublePercentages['11']}%"
              ></div>
            </div>
            <span class="progress-value">{doublePercentages["11"]}%</span>
          </div>
        </div>

        <p class="theory-text">
          📐 Theoretical probability: 25% each | Total: {doubleStats.total} measurements
        </p>

        {#if doubleHistory.length > 0}
          <div class="history-section">
            <h4>Recent Results</h4>
            <div class="history-chips">
              {#each doubleHistory as result, i}
                <span
                  class="chip outcome-{result}"
                  style="animation-delay: {i * 0.02}s"
                >
                  {getOutcomeEmoji(result)}
                </span>
              {/each}
            </div>
          </div>
        {/if}
      </div>
    {/if}
  </div>

  <!-- Educational Note -->
  <div class="edu-note">
    {#if mode === "single"}
      <div class="note-icon"></div>
      <div class="note-content">
        <h4>What You're Learning</h4>
        <p>
          <strong>Superposition:</strong> Before measurement, the qubit exists in
          BOTH |0⟩ and |1⟩ states simultaneously. The Hadamard gate creates perfect
          50/50 probability - this is true quantum randomness!
        </p>
      </div>
    {:else}
      <div class="note-icon"></div>
      <div class="note-content">
        <h4>Quantum Power: Exponential States!</h4>
        <p>
          <strong>With 2 qubits, we get 4 states.</strong> With N qubits, we get
          2ᴺ states! This is why quantum computers can process many possibilities
          at once.
        </p>
        <p class="note-detail">
          <em
            >Note: These coins are independent (not entangled). Each flips
            randomly on its own.</em
          >
        </p>
      </div>
    {/if}
  </div>
</div>

<style>
  .quantum-demo {
    display: flex;
    flex-direction: column;
    gap: 24px;
  }

  /* Mode Tabs */
  .mode-tabs {
    display: flex;
    gap: 16px;
    justify-content: center;
  }

  .mode-tab {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 16px 24px;
    background: white;
    border: 3px solid #e2e8f0;
    border-radius: 16px;
    cursor: pointer;
    transition: all 0.3s ease;
    min-width: 200px;
  }

  :global([data-theme="dark"]) .mode-tab {
    background: var(--color-surface);
    border-color: var(--color-border);
    color: var(--color-text-primary);
  }

  .mode-tab:hover {
    border-color: #667eea;
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.2);
  }

  .mode-tab.active {
    border-color: #667eea;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
  }

  .tab-icon {
    font-size: 32px;
  }

  .tab-content {
    display: flex;
    flex-direction: column;
    text-align: left;
  }

  .tab-title {
    font-weight: 700;
    font-size: 16px;
  }

  .tab-subtitle {
    font-size: 12px;
    opacity: 0.8;
  }

  /* Circuit Card */
  .circuit-card {
    background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
    border-radius: 16px;
    overflow: hidden;
    border: 1px solid #e2e8f0;
  }

  :global([data-theme="dark"]) .circuit-card {
    background: linear-gradient(
      135deg,
      rgba(30, 41, 59, 0.5) 0%,
      rgba(15, 23, 42, 0.5) 100%
    );
    border-color: var(--color-border);
  }

  .circuit-header {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    padding: 12px 20px;
  }

  .circuit-header h3 {
    margin: 0;
    color: white;
    font-size: 16px;
  }

  .circuit-content {
    padding: 20px;
  }

  .circuit-diagram {
    background: #1a1a2e;
    padding: 16px 24px;
    border-radius: 8px;
    font-family: "Courier New", monospace;
    margin-bottom: 12px;
  }

  .circuit-line {
    display: flex;
    align-items: center;
    gap: 4px;
    color: #00ff88;
    font-size: 14px;
    margin: 8px 0;
  }

  .qubit-label {
    color: #ffd700;
    font-weight: bold;
  }

  .wire {
    color: #666;
  }

  .gate {
    padding: 4px 8px;
    border-radius: 4px;
    font-weight: bold;
  }

  .gate.hadamard {
    background: #667eea;
    color: white;
  }

  .measure {
    font-size: 16px;
  }

  .output {
    color: #00ff88;
    font-weight: bold;
  }

  .circuit-explain {
    margin: 0;
    color: #475569;
    font-size: 14px;
  }

  :global([data-theme="dark"]) .circuit-explain {
    color: var(--color-text-secondary);
  }

  .circuit-explain code {
    background: #e2e8f0;
    padding: 2px 6px;
    border-radius: 4px;
    font-family: "Courier New", monospace;
  }

  :global([data-theme="dark"]) .circuit-explain code {
    background: var(--color-border);
    color: var(--color-text-primary);
  }

  /* Error Box */
  .error-box {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 16px;
    background: #fef2f2;
    border: 1px solid #fecaca;
    border-radius: 12px;
    color: #dc2626;
  }

  .error-icon {
    font-size: 24px;
  }

  .error-box p {
    margin: 0;
  }

  /* Coin Display Area */
  .coin-display-area {
    background: linear-gradient(180deg, #f1f5f9 0%, #e2e8f0 100%);
    border-radius: 20px;
    padding: 40px;
    display: flex;
    justify-content: center;
    min-height: 220px;
    overflow: hidden;
  }

  :global([data-theme="dark"]) .coin-display-area {
    background: linear-gradient(
      180deg,
      rgba(30, 41, 59, 0.3) 0%,
      rgba(15, 23, 42, 0.3) 100%
    );
  }

  .single-coin-container,
  .double-coin-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
    max-width: 100%;
  }

  .coin-pair {
    display: flex;
    align-items: center;
    gap: 24px;
    max-width: 100%;
  }

  .coin-unit {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
    max-width: 120px;
  }

  .coin-separator {
    display: flex;
    align-items: center;
  }

  .tensor {
    font-size: 28px;
    color: #667eea;
    font-weight: bold;
  }

  .coin-name {
    font-size: 13px;
    color: #64748b;
    font-weight: 600;
  }

  :global([data-theme="dark"]) .coin-name {
    color: var(--color-text-secondary);
  }

  /* 3D Coin */
  .coin-wrapper-3d {
    perspective: 1000px;
    width: 100px;
    height: 100px;
  }

  .coin-wrapper-3d.spinning {
    animation: none;
  }

  .coin-wrapper-3d.spinning .coin-3d {
    animation: spin3d 0.6s linear infinite;
  }

  .coin-wrapper-3d.batch-spinning .coin-3d {
    animation: spin3d 0.2s linear infinite;
  }

  .coin-3d {
    width: 100px;
    height: 100px;
    position: relative;
    transform-style: preserve-3d;
    transition: transform 0.6s ease;
  }

  .coin-3d.measured {
    animation: bounce 0.5s ease;
  }

  .coin-3d.show-tails {
    transform: rotateY(180deg);
  }

  .coin-side {
    position: absolute;
    width: 100%;
    height: 100%;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    backface-visibility: hidden;
    box-shadow:
      0 10px 30px rgba(0, 0, 0, 0.2),
      inset 0 -5px 20px rgba(0, 0, 0, 0.1);
  }

  .coin-heads {
    background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
  }

  .coin-tails {
    background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
    transform: rotateY(180deg);
  }

  .coin-letter {
    font-size: 42px;
    color: white;
    font-weight: bold;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
  }

  @keyframes spin3d {
    0% {
      transform: rotateY(0deg);
    }
    100% {
      transform: rotateY(360deg);
    }
  }

  @keyframes bounce {
    0%,
    100% {
      transform: scale(1);
    }
    50% {
      transform: scale(1.1);
    }
  }

  /* Keep show-tails transform when bouncing */
  .coin-3d.measured.show-tails {
    animation: bounce-tails 0.5s ease;
  }

  @keyframes bounce-tails {
    0%,
    100% {
      transform: rotateY(180deg) scale(1);
    }
    50% {
      transform: rotateY(180deg) scale(1.1);
    }
  }

  .batch-text {
    color: #667eea;
    animation: pulse 0.5s ease-in-out infinite;
  }

  @keyframes pulse {
    0%,
    100% {
      opacity: 1;
    }
    50% {
      opacity: 0.5;
    }
  }

  /* State Label */
  .state-label {
    text-align: center;
  }

  .state-text {
    display: block;
    font-family: "Courier New", monospace;
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 4px;
  }

  .superposition-text {
    color: #667eea;
  }

  .measured-text {
    color: #059669;
  }

  .state-description {
    font-size: 13px;
    color: #64748b;
  }

  :global([data-theme="dark"]) .state-description {
    color: var(--color-text-secondary);
  }

  /* Control Buttons */
  .control-buttons {
    display: flex;
    gap: 16px;
    justify-content: center;
    flex-wrap: wrap;
  }

  /* Stats Section */
  .stats-section {
    background: white;
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
  }

  :global([data-theme="dark"]) .stats-section {
    background: var(--color-surface);
  }

  .stats-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }

  .stats-header h3 {
    margin: 0;
    color: #1e293b;
  }

  :global([data-theme="dark"]) .stats-header h3 {
    color: var(--color-text-primary);
  }

  .clear-btn {
    padding: 8px 16px;
    background: #f1f5f9;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    font-size: 13px;
    color: #64748b;
    cursor: pointer;
    transition: all 0.2s;
  }

  :global([data-theme="dark"]) .clear-btn {
    background: var(--color-bg-secondary);
    border-color: var(--color-border);
    color: var(--color-text-secondary);
  }

  .clear-btn:hover {
    background: #e2e8f0;
    color: #475569;
  }

  :global([data-theme="dark"]) .clear-btn:hover {
    background: var(--color-border);
    color: var(--color-text-primary);
  }

  /* Stat Cards */
  .stat-cards-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin-bottom: 24px;
  }

  .stat-cards-row.four {
    grid-template-columns: repeat(4, 1fr);
  }

  .stat-card {
    padding: 16px;
    border-radius: 12px;
    text-align: center;
    display: flex;
    flex-direction: column;
    gap: 4px;
  }

  .stat-card.total {
    background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
  }

  .stat-card.heads,
  .stat-card.outcome-00 {
    background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
  }

  .stat-card.tails,
  .stat-card.outcome-11 {
    background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
  }

  .stat-card.outcome-01 {
    background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
  }

  .stat-card.outcome-10 {
    background: linear-gradient(135deg, #fce7f3 0%, #fbcfe8 100%);
  }

  .stat-emoji {
    font-size: 20px;
  }

  .stat-value {
    font-size: 28px;
    font-weight: bold;
    color: #1e293b;
  }

  :global([data-theme="dark"]) .stat-value {
    color: var(--color-text-primary);
  }

  .stat-label {
    font-size: 12px;
    color: #64748b;
    font-weight: 500;
  }

  :global([data-theme="dark"]) .stat-label {
    color: var(--color-text-secondary);
  }

  .stat-percent {
    font-size: 14px;
    font-weight: 600;
    color: #475569;
  }

  :global([data-theme="dark"]) .stat-percent {
    color: var(--color-text-secondary);
  }

  /* Progress Bars */
  .progress-bars {
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-bottom: 16px;
  }

  .progress-item {
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .progress-label {
    width: 50px;
    font-size: 13px;
    font-weight: 600;
    color: #475569;
    font-family: "Courier New", monospace;
  }

  :global([data-theme="dark"]) .progress-label {
    color: var(--color-text-secondary);
  }

  .progress-track {
    flex: 1;
    height: 24px;
    background: #f1f5f9;
    border-radius: 12px;
    overflow: hidden;
  }

  :global([data-theme="dark"]) .progress-track {
    background: var(--color-border);
  }

  .progress-fill {
    height: 100%;
    border-radius: 12px;
    transition: width 0.5s ease;
  }

  .progress-fill.heads,
  .progress-fill.outcome-00 {
    background: linear-gradient(90deg, #fbbf24, #f59e0b);
  }

  .progress-fill.tails,
  .progress-fill.outcome-11 {
    background: linear-gradient(90deg, #3b82f6, #1d4ed8);
  }

  .progress-fill.outcome-01 {
    background: linear-gradient(90deg, #10b981, #059669);
  }

  .progress-fill.outcome-10 {
    background: linear-gradient(90deg, #ec4899, #db2777);
  }

  .progress-value {
    width: 50px;
    font-size: 13px;
    font-weight: 600;
    color: #475569;
    text-align: right;
  }

  :global([data-theme="dark"]) .progress-value {
    color: var(--color-text-secondary);
  }

  .theory-text {
    text-align: center;
    color: #64748b;
    font-size: 13px;
    margin: 0;
  }

  :global([data-theme="dark"]) .theory-text {
    color: var(--color-text-primary);
  }

  /* History Section */
  .history-section {
    margin-top: 20px;
    padding-top: 20px;
    border-top: 1px solid #e2e8f0;
  }

  :global([data-theme="dark"]) .history-section {
    border-top-color: var(--color-border);
  }

  .history-section h4 {
    margin: 0 0 12px 0;
    font-size: 14px;
    color: #475569;
  }

  :global([data-theme="dark"]) .history-section h4 {
    color: var(--color-text-primary);
  }

  .history-dots {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }

  .dot {
    width: 28px;
    height: 28px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 11px;
    font-weight: bold;
    color: white;
    animation: popIn 0.3s ease;
  }

  .dot.heads {
    background: #f59e0b;
  }

  .dot.tails {
    background: #3b82f6;
  }

  .history-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
  }

  .chip {
    padding: 6px 10px;
    border-radius: 20px;
    font-size: 14px;
    animation: popIn 0.3s ease;
  }

  .chip.outcome-00 {
    background: #fef3c7;
  }
  .chip.outcome-01 {
    background: #d1fae5;
  }
  .chip.outcome-10 {
    background: #fce7f3;
  }
  .chip.outcome-11 {
    background: #dbeafe;
  }

  @keyframes popIn {
    0% {
      transform: scale(0);
      opacity: 0;
    }
    100% {
      transform: scale(1);
      opacity: 1;
    }
  }

  /* Educational Note */
  .edu-note {
    display: flex;
    gap: 16px;
    padding: 20px;
    background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);
    border-radius: 16px;
    border: 1px solid #a7f3d0;
  }

  .note-icon {
    font-size: 32px;
  }

  .note-content h4 {
    margin: 0 0 8px 0;
    color: #065f46;
  }

  .note-content p {
    margin: 0 0 8px 0;
    color: #047857;
    font-size: 14px;
    line-height: 1.5;
  }

  .note-detail {
    font-size: 13px !important;
    color: #059669 !important;
  }

  /* Responsive */
  @media (max-width: 700px) {
    .mode-tabs {
      flex-direction: column;
      align-items: stretch;
    }

    .mode-tab {
      min-width: auto;
    }

    .stat-cards-row.four {
      grid-template-columns: repeat(2, 1fr);
    }

    .coin-3d {
      width: 80px;
      height: 80px;
    }

    .question,
    .result-letter {
      font-size: 32px;
    }

    .coin-pair {
      gap: 16px;
    }
  }
</style>
