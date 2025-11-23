<script>
  import './entanglementDemo.css';
  import Button from "../ui/Button.svelte";
  import Card from "../ui/Card.svelte";
  import StatCard from "../ui/StatCard.svelte";

  let bellState = $state("phi_plus"); // phi_plus, psi_plus, phi_minus, psi_minus
  let measurements = $state([]);
  let isFlipping = $state(false);
  let totalFlips = $state(0);
  let aliceResult = $state(null);
  let bobResult = $state(null);
  let results = $state({
    "00": 0,
    "01": 0,
    "10": 0,
    "11": 0,
  });

  // Debug reactive statement
  $effect(() => {
    console.log("Alice Result:", aliceResult, "Bob Result:", bobResult, "isFlipping:", isFlipping);
  });

  const bellStates = {
    phi_plus: {
      name: "Φ⁺",
      formula: "(|00⟩ + |11⟩)/√2",
      description: "Alice & Bob always get the SAME result",
      humanDescription: "When Alice measures 0, Bob gets 0. When Alice measures 1, Bob gets 1.",
      expected: { "00": 0.5, "01": 0, "10": 0, "11": 0.5 },
    },
    psi_plus: {
      name: "Ψ⁺",
      formula: "(|01⟩ + |10⟩)/√2",
      description: "Alice & Bob always get OPPOSITE results",
      humanDescription: "When Alice measures 0, Bob gets 1. When Alice measures 1, Bob gets 0.",
      expected: { "00": 0, "01": 0.5, "10": 0.5, "11": 0 },
    },
    phi_minus: {
      name: "Φ⁻",
      formula: "(|00⟩ - |11⟩)/√2",
      description: "Alice & Bob always MATCH (with quantum phase)",
      humanDescription: "Just like Φ⁺, they always get the same result!",
      expected: { "00": 0.5, "01": 0, "10": 0, "11": 0.5 },
    },
    psi_minus: {
      name: "Ψ⁻",
      formula: "(|01⟩ - |10⟩)/√2",
      description: "Alice & Bob always DIFFER (with quantum phase)",
      humanDescription: "Just like Ψ⁺, they always get opposite results!",
      expected: { "00": 0, "01": 0.5, "10": 0.5, "11": 0 },
    },
  };

  async function measureEntangledPair() {
    if (isFlipping) return;
    isFlipping = true;

    try {
      const response = await fetch("http://localhost:8000/api/bell-state-measure", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ state: bellState }),
      });

      const data = await response.json();
      console.log("API Response:", data);
      
      // The API returns result as a string like "11" or "01"
      const resultString = data.result;
      console.log("Result string:", resultString);
      
      // Parse the result string
      aliceResult = parseInt(resultString[0]);
      bobResult = parseInt(resultString[1]);
      
      console.log("Alice:", aliceResult, "Bob:", bobResult);

      results[resultString]++;
      totalFlips++;
      measurements = [resultString, ...measurements].slice(0, 10);
      
      setTimeout(() => {
        isFlipping = false;
      }, 600);
    } catch (error) {
      console.error("Error measuring entangled pair:", error);
      isFlipping = false;
    }
  }

  async function measureBatch(count) {
    isFlipping = true;

    try {
      const response = await fetch("http://localhost:8000/api/bell-state-batch", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ state: bellState, shots: count }),
      });

      const data = await response.json();
      const counts = data.counts; // e.g., {"00": 48, "11": 52}

      Object.keys(counts).forEach((key) => {
        results[key] += counts[key];
      });
      totalFlips += count;

      // Add latest results to measurements
      const latestResults = Object.entries(counts)
        .flatMap(([outcome, count]) => Array(Math.min(count, 10)).fill(outcome))
        .slice(0, 10);
      measurements = [...latestResults, ...measurements].slice(0, 10);
      
      // Show the last measurement visually
      if (latestResults.length > 0) {
        const lastResult = latestResults[0];
        aliceResult = parseInt(lastResult[0]);
        bobResult = parseInt(lastResult[1]);
      }
    } catch (error) {
      console.error("Error measuring batch:", error);
    } finally {
      setTimeout(() => {
        isFlipping = false;
      }, 500);
    }
  }

  function reset() {
    measurements = [];
    totalFlips = 0;
    aliceResult = null;
    bobResult = null;
    results = { "00": 0, "01": 0, "10": 0, "11": 0 };
  }

  function changeBellState(state) {
    bellState = state;
    reset();
  }

  let percentages = $derived({
    "00": totalFlips > 0 ? ((results["00"] / totalFlips) * 100).toFixed(1) : "0.0",
    "01": totalFlips > 0 ? ((results["01"] / totalFlips) * 100).toFixed(1) : "0.0",
    "10": totalFlips > 0 ? ((results["10"] / totalFlips) * 100).toFixed(1) : "0.0",
    "11": totalFlips > 0 ? ((results["11"] / totalFlips) * 100).toFixed(1) : "0.0",
  });

  let percentagesNum = $derived({
    "00": totalFlips > 0 ? ((results["00"] / totalFlips) * 100) : 0,
    "01": totalFlips > 0 ? ((results["01"] / totalFlips) * 100) : 0,
    "10": totalFlips > 0 ? ((results["10"] / totalFlips) * 100) : 0,
    "11": totalFlips > 0 ? ((results["11"] / totalFlips) * 100) : 0,
  });

  let currentState = $derived(bellStates[bellState]);
</script>

<div class="entanglement-demo">
  <Card>
    <h3>🔬 Quantum Entanglement: Alice on Earth 🌍 & Bob on Mars 🔴</h3>
    <p class="intro-text">
      Alice and Bob share entangled quantum particles. Even though they're millions of kilometers apart,
      when one measures their particle, it <strong>instantly affects</strong> what the other will measure!
    </p>

    <div class="bell-state-selector">
      <p class="selector-label">🎯 Choose the Entanglement Type (This Changes The Results!):</p>
      <div class="state-buttons">
        {#each Object.entries(bellStates) as [key, state]}
          <button
            class="state-button"
            class:active={bellState === key}
            onclick={() => changeBellState(key)}
            disabled={isFlipping}
          >
            <div class="state-name">{state.name}</div>
            <div class="state-formula">{state.formula}</div>
            <div class="state-simple">{state.description}</div>
          </button>
        {/each}
      </div>
      <div class="current-selection">
        ⭐ Currently selected: <strong>{currentState.name}</strong> - {currentState.humanDescription}
      </div>
    </div>

    <div class="current-state-info">
      <h4>📡 Current Entanglement: {currentState.name} State</h4>
      <p class="human-description">
        <strong>What this means:</strong> {currentState.humanDescription}
      </p>
      <p class="formula-detail">
        <em>Technical formula: {currentState.formula}</em>
      </p>
    </div>
  </Card>

  <div class="visualization">
    <Card>
      <h4 class="viz-title">🌌 Alice & Bob Measuring Their Entangled Particles</h4>
      <div class="space-scene">
        <!-- Alice on Earth -->
        <div class="person-container alice-container" class:measuring={isFlipping}>
          <div class="planet earth">🌍</div>
          <div class="person-label">Alice on Earth</div>
          <div class="measurement-box" class:has-result={aliceResult !== null}>
            <div class="person-icon">👩‍🔬</div>
            <div class="particle-result">
              {#if aliceResult !== null}
                <span class="result-value" class:result-0={aliceResult === 0} class:result-1={aliceResult === 1}>
                  {aliceResult}
                </span>
              {:else}
                <span class="result-pending">?</span>
              {/if}
            </div>
          </div>
        </div>

        <!-- Entanglement Connection -->
        <div class="entanglement-connection">
          <div class="distance-label">
            <div class="distance-text">~225 Million km</div>
            <div class="distance-subtext">Light takes 12.5 minutes</div>
          </div>
          <div class="connection-line" class:active={isFlipping}>
            <div class="quantum-waves"></div>
            <div class="instant-label" class:show={isFlipping}>⚡ Instant Correlation!</div>
          </div>
        </div>

        <!-- Bob on Mars -->
        <div class="person-container bob-container" class:measuring={isFlipping}>
          <div class="planet mars">🪐</div>
          <div class="person-label">Bob on Mars</div>
          <div class="measurement-box" class:has-result={bobResult !== null}>
            <div class="person-icon">👨‍🔬</div>
            <div class="particle-result">
              {#if bobResult !== null}
                <span class="result-value" class:result-0={bobResult === 0} class:result-1={bobResult === 1}>
                  {bobResult}
                </span>
              {:else}
                <span class="result-pending">?</span>
              {/if}
            </div>
          </div>
        </div>
      </div>

      {#if aliceResult !== null && bobResult !== null}
        <div class="result-explanation">
          <div class="result-header">
            {#if aliceResult === bobResult}
              <span class="result-icon">✅</span>
              <strong>MATCHED!</strong>
            {:else}
              <span class="result-icon">🔄</span>
              <strong>OPPOSITE!</strong>
            {/if}
          </div>
          <p class="correlation-text">
            Alice measured <span class="result-badge result-{aliceResult}">{aliceResult}</span> on Earth,
            Bob measured <span class="result-badge result-{bobResult}">{bobResult}</span> on Mars
          </p>
          <p class="explanation-detail">
            {#if aliceResult === bobResult}
              {#if currentState.name === "Φ⁺" || currentState.name === "Φ⁻"}
                🎉 Perfect! The {currentState.name} state makes them <strong>always match</strong>.
              {:else}
                🤔 Unexpected! The {currentState.name} state should make them differ.
              {/if}
            {:else}
              {#if currentState.name === "Ψ⁺" || currentState.name === "Ψ⁻"}
                🎉 Perfect! The {currentState.name} state makes them <strong>always opposite</strong>.
              {:else}
                🤔 Unexpected! The {currentState.name} state should make them match.
              {/if}
            {/if}
          </p>
          <div class="spooky-fact">
            👻 <strong>Spooky Action:</strong> Even though they're 225 million km apart, 
            measuring one <em>instantly</em> determines what the other will measure!
          </div>
        </div>
      {/if}
    </Card>
  </div>

  <div class="controls">
    <Button onclick={measureEntangledPair} disabled={isFlipping}>
      {isFlipping ? "🔬 Measuring..." : "📡 Measure Particles!"}
    </Button>
    <Button onclick={() => measureBatch(10)} disabled={isFlipping} variant="secondary">
      Measure 10x
    </Button>
    <Button onclick={() => measureBatch(100)} disabled={isFlipping} variant="secondary">
      Measure 100x
    </Button>
    <Button onclick={reset} disabled={isFlipping || totalFlips === 0} variant="secondary">
      🔄 Reset
    </Button>
  </div>

  {#if totalFlips >= 0}
    <Card>
      <div class="beginner-explainer">
        <h4>🎯 What Are You Seeing?</h4>
        <div class="explainer-grid">
          <div class="explainer-item">
            <span class="explainer-icon">🎲</span>
            <div>
              <strong>Random but Correlated</strong>
              <p>Each measurement is random, but Alice and Bob's results are mysteriously linked!</p>
            </div>
          </div>
          <div class="explainer-item">
            <span class="explainer-icon">📊</span>
            <div>
              <strong>Statistics Reveal Patterns</strong>
              <p>Run 100+ measurements to see the quantum correlation pattern emerge</p>
            </div>
          </div>
          <div class="explainer-item">
            <span class="explainer-icon">🎯</span>
            <div>
              <strong>Bell State Controls Pattern</strong>
              <p>Different Bell states create different correlation patterns (match or opposite)</p>
            </div>
          </div>
          <div class="explainer-item">
            <span class="explainer-icon">✨</span>
            <div>
              <strong>50/50 Randomness</strong>
              <p>For Φ⁺: ~50% both get 0, ~50% both get 1. Perfectly random, but perfectly linked!</p>
            </div>
          </div>
        </div>
      </div>
    </Card>

    <Card>
      <div class="stats-explainer">
        <h4>📊 Understanding the Statistics</h4>
        <div class="concept-box">
          <p><strong>What's happening:</strong> When you click "Measure 100x", the computer runs 100 quantum measurements. Each time:</p>
          <ol>
            <li>Alice and Bob both measure their entangled particles</li>
            <li>Each gets either 0 or 1 (random)</li>
            <li>But their results are <em>correlated</em> based on the Bell state</li>
          </ol>
          
          <div class="example-box">
            <strong>Example with Φ⁺ state (currently selected):</strong>
            <ul>
              <li><strong>Both get 0:</strong> ~50 times (Alice: 0, Bob: 0)</li>
              <li><strong>Both get 1:</strong> ~50 times (Alice: 1, Bob: 1)</li>
              <li><strong>Different results:</strong> ~0 times (they ALWAYS match!)</li>
            </ul>
            <p class="key-point">🔑 Key: You can't predict if they'll get 0 or 1, but you KNOW they'll match!</p>
          </div>

          <div class="try-this">
            <strong>🧪 Try this:</strong> Switch to <strong>Ψ⁺</strong> state and click "Measure 100x"<br/>
            Now they'll ALWAYS get opposite results (0↔1 or 1↔0) instead of matching!
          </div>
        </div>
      </div>
    </Card>

    <Card title="📈 Measurement Statistics">
      <div class="stats-grid">
        <StatCard label="Total Measurements" value={String(totalFlips)} />
        <StatCard
          label="Both 0 (|00⟩)"
          value={String(results["00"])}
          subtext="{percentages['00']}%"
        />
        <StatCard
          label="Alice:0 Bob:1 (|01⟩)"
          value={String(results["01"])}
          subtext="{percentages['01']}%"
        />
        <StatCard
          label="Alice:1 Bob:0 (|10⟩)"
          value={String(results["10"])}
          subtext="{percentages['10']}%"
        />
        <StatCard
          label="Both 1 (|11⟩)"
          value={String(results["11"])}
          subtext="{percentages['11']}%"
        />
      </div>

      <div class="expected-vs-actual">
        <h5>📈 Expected vs Actual for {currentState.name} State:</h5>
        <div class="comparison-grid">
          <div class="comparison-item">
            <span class="outcome-label">|00⟩:</span>
            <span class="expected">Expected {(currentState.expected['00'] * 100).toFixed(0)}%</span>
            <span class="actual" class:close={Math.abs(percentagesNum['00'] - currentState.expected['00'] * 100) < 10}>Actual {percentages['00']}%</span>
          </div>
          <div class="comparison-item">
            <span class="outcome-label">|01⟩:</span>
            <span class="expected">Expected {(currentState.expected['01'] * 100).toFixed(0)}%</span>
            <span class="actual" class:close={Math.abs(percentagesNum['01'] - currentState.expected['01'] * 100) < 10}>Actual {percentages['01']}%</span>
          </div>
          <div class="comparison-item">
            <span class="outcome-label">|10⟩:</span>
            <span class="expected">Expected {(currentState.expected['10'] * 100).toFixed(0)}%</span>
            <span class="actual" class:close={Math.abs(percentagesNum['10'] - currentState.expected['10'] * 100) < 10}>Actual {percentages['10']}%</span>
          </div>
          <div class="comparison-item">
            <span class="outcome-label">|11⟩:</span>
            <span class="expected">Expected {(currentState.expected['11'] * 100).toFixed(0)}%</span>
            <span class="actual" class:close={Math.abs(percentagesNum['11'] - currentState.expected['11'] * 100) < 10}>Actual {percentages['11']}%</span>
          </div>
        </div>
        <p class="quantum-note">
          💡 <strong>Notice:</strong> As you run more measurements, the percentages get closer to the expected values!
        </p>
      </div>

      <div class="measurement-history">
        <h5>📜 Last 10 Measurements</h5>
        <div class="history-list">
          {#each measurements.filter(m => m && m.length === 2) as measurement, i}
            <div class="history-chip" style="animation-delay: {i * 0.05}s">
              <span class="chip-alice">{measurement.charAt(0)}</span>
              <span class="chip-bob">{measurement.charAt(1)}</span>
            </div>
          {/each}
        </div>
      </div>
    </Card>
  {/if}
</div>
