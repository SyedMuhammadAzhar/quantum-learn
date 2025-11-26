<script>
  import './measurementDemo.css';
  import Button from "../ui/Button.svelte";
  import Card from "../ui/Card.svelte";
  import StatCard from "../ui/StatCard.svelte";

  let selectedState = "equal";
  let selectedBasis = "z";
  let isMeasuring = false;
  let totalMeasurements = 0;
  let results = {
    "0": 0,
    "1": 0,
  };
  let measurements = [];
  let quantumState = "superposition"; // superposition, measuring, collapsed
  let collapsedValue = null;
  
  // Mystery Box game state
  let gameStarted = false;
  let gameSecret = null;
  let gamePulls = 0;
  let gameResults = { "0": 0, "1": 0 };
  let gameBalls = [];
  let hasGuessed = false;
  let gameGuess = null;
  let showGameResult = false;
  let gameCorrect = false;
  
  const gameStateNames = {
    equal: "Mixed Equally (50-50)",
    biased_0: "Mostly Red Balls",
    biased_1: "Mostly Blue Balls",
    definite_0: "Only Red Balls",
    definite_1: "Only Blue Balls"
  };

  const quantumStates = {
    equal: {
      name: "Equal Superposition",
      formula: "(|0⟩ + |1⟩)/√2",
      description: "50% chance of 0, 50% chance of 1",
      color: "#667eea",
      zBasis: { prob0: 50, prob1: 50 },
      xBasis: { prob0: 100, prob1: 0 },  // |+⟩ state always gives + in X-basis
    },
    biased_0: {
      name: "Biased Toward 0",
      formula: "(√3|0⟩ + |1⟩)/2",
      description: "75% chance of 0, 25% chance of 1",
      color: "#3b82f6",
      zBasis: { prob0: 75, prob1: 25 },
      xBasis: { prob0: 50, prob1: 50 },  // Mixed state in X-basis
    },
    biased_1: {
      name: "Biased Toward 1",
      formula: "(|0⟩ + √3|1⟩)/2",
      description: "25% chance of 0, 75% chance of 1",
      color: "#8b5cf6",
      zBasis: { prob0: 25, prob1: 75 },
      xBasis: { prob0: 50, prob1: 50 },  // Mixed state in X-basis
    },
    definite_0: {
      name: "Definite 0",
      formula: "|0⟩",
      description: "100% chance of 0",
      color: "#10b981",
      zBasis: { prob0: 100, prob1: 0 },
      xBasis: { prob0: 50, prob1: 50 },  // |0⟩ in X-basis = 50-50
    },
    definite_1: {
      name: "Definite 1",
      formula: "|1⟩",
      description: "100% chance of 1",
      color: "#f59e0b",
      zBasis: { prob0: 0, prob1: 100 },
      xBasis: { prob0: 50, prob1: 50 },  // |1⟩ in X-basis = 50-50
    },
  };

  const measurementBases = {
    z: {
      name: "Z-Basis (Computational)",
      icon: "📊",
      description: "Standard 0 or 1 measurement",
    },
    x: {
      name: "X-Basis (Hadamard)",
      icon: "✖️",
      description: "Measures in + or - basis",
    },
  };

  async function performMeasurement() {
    isMeasuring = true;
    quantumState = "measuring";
    collapsedValue = null;
    
    await new Promise(resolve => setTimeout(resolve, 600));
    
    try {
      const response = await fetch("http://localhost:8000/api/measure-qubit", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
          state: selectedState,
          basis: selectedBasis 
        }),
      });

      if (!response.ok) {
        const error = await response.text();
        console.error("API Error:", response.status, error);
        alert(`Error: ${response.status} - ${error}`);
        throw new Error(`HTTP ${response.status}`);
      }

      const data = await response.json();
      console.log("Measurement response:", data);
      const result = String(data.result);

      quantumState = "collapsed";
      collapsedValue = result;
      results[result] = (results[result] || 0) + 1;
      totalMeasurements = totalMeasurements + 1;
      measurements = [result, ...measurements].slice(0, 10);
      
      results = {...results};
      
      // Keep the collapsed state visible until next measurement
    } catch (error) {
      console.error("Error:", error);
      quantumState = "superposition";
    } finally {
      isMeasuring = false;
    }
  }

  async function measureBatch(count) {
    isMeasuring = true;

    try {
      const response = await fetch("http://localhost:8000/api/measure-qubit-batch", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
          state: selectedState,
          basis: selectedBasis,
          shots: count 
        }),
      });

      const data = await response.json();
      console.log("Batch measurement response:", data);
      const counts = data.counts;

      results["0"] = (results["0"] || 0) + (counts["0"] || 0);
      results["1"] = (results["1"] || 0) + (counts["1"] || 0);
      totalMeasurements = totalMeasurements + count;
      
      for (let i = 0; i < Math.min(10, count); i++) {
        const randomKey = Math.random() < ((counts["0"] || 0) / count) ? "0" : "1";
        measurements = [randomKey, ...measurements];
      }
      measurements = measurements.slice(0, 10);
      
      results = {...results};
    } catch (error) {
      console.error("Error:", error);
    } finally {
      isMeasuring = false;
    }
  }

  function reset() {
    measurements = [];
    totalMeasurements = 0;
    results = { "0": 0, "1": 0 };
    quantumState = "superposition";
    collapsedValue = null;
  }

  function changeState(state) {
    selectedState = state;
    reset();
  }

  function changeBasis(basis) {
    selectedBasis = basis;
    reset();
  }

  $: percentages = {
    "0": totalMeasurements > 0 ? ((results["0"] / totalMeasurements) * 100).toFixed(1) : 0,
    "1": totalMeasurements > 0 ? ((results["1"] / totalMeasurements) * 100).toFixed(1) : 0,
  };

  $: currentStateInfo = quantumStates[selectedState];
  $: currentBasisInfo = measurementBases[selectedBasis];
  $: expectedProbs = selectedBasis === 'z' ? currentStateInfo.zBasis : currentStateInfo.xBasis;
  $: expectedDescription = `${expectedProbs.prob0}% chance of 0, ${expectedProbs.prob1}% chance of 1`;
  
  function startGame() {
    const states = Object.keys(quantumStates);
    gameSecret = states[Math.floor(Math.random() * states.length)];
    gameStarted = true;
    gamePulls = 0;
    gameResults = { "0": 0, "1": 0 };
    gameBalls = [];
    hasGuessed = false;
    gameGuess = null;
    showGameResult = false;
    gameCorrect = false;
  }
  
  async function pullBall() {
    if (gamePulls >= 10) return;
    
    isMeasuring = true;
    
    try {
      const response = await fetch("http://localhost:8000/api/measure-qubit", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
          state: gameSecret,
          basis: "z"
        }),
      });

      const data = await response.json();
      console.log("Game pull response:", data);
      const result = String(data.result);
      
      gameResults[result] = (gameResults[result] || 0) + 1;
      gamePulls++;
      gameBalls = [...gameBalls, result];
      gameResults = {...gameResults};
    } catch (error) {
      console.error("Error:", error);
    } finally {
      isMeasuring = false;
    }
  }
  
  function makeSimpleGuess(guess) {
    gameGuess = guess;
    hasGuessed = true;
    gameCorrect = guess === gameSecret;
    showGameResult = true;
  }
</script>

<div class="measurement-demo">
  <Card>
    <h3>🔬 Quantum Measurement Lab</h3>
    <p>Pick a quantum state and measure it! Each state has different probabilities:</p>
    <div class="state-guide">
      <span>🟢 <strong>Equal:</strong> 50% get 0, 50% get 1</span>
      <span>🔵 <strong>Biased to 0:</strong> 75% get 0, 25% get 1</span>
      <span>🟣 <strong>Biased to 1:</strong> 25% get 0, 75% get 1</span>
      <span>✅ <strong>Always 0:</strong> 100% get 0</span>
      <span>🟠 <strong>Always 1:</strong> 100% get 1</span>
    </div>

    <div class="state-selector">
      <p class="selector-label">1️⃣ Choose Quantum State:</p>
      <div class="state-buttons">
        {#each Object.entries(quantumStates) as [key, state]}
          <button
            class="state-button"
            class:active={selectedState === key}
            style="border-color: {state.color}"
            onclick={() => changeState(key)}
            disabled={isMeasuring}
          >
            <div class="state-name">{state.name}</div>
            <div class="state-formula">{state.formula}</div>
          </button>
        {/each}
      </div>
    </div>

    <div class="basis-selector">
      <p class="selector-label">2️⃣ Choose Measurement Basis:</p>
      <div class="basis-buttons">
        {#each Object.entries(measurementBases) as [key, basis]}
          <button
            class="basis-button"
            class:active={selectedBasis === key}
            onclick={() => changeBasis(key)}
            disabled={isMeasuring}
          >
            <div class="basis-icon">{basis.icon}</div>
            <div class="basis-name">{basis.name}</div>
          </button>
        {/each}
      </div>
    </div>

    <div class="current-setup">
      <h4>Current Setup:</h4>
      <p class="formula">{currentStateInfo.formula}</p>
      <p class="basis-info">Measuring in: <strong>{currentBasisInfo.name}</strong></p>
      <p class="description">Expected outcome: <strong>{expectedDescription}</strong></p>
      {#if selectedBasis === 'x' && (selectedState === 'definite_0' || selectedState === 'definite_1')}
        <p class="basis-warning">⚡ Different basis = Different results! Even a "definite" state becomes uncertain in a different measurement basis.</p>
      {/if}
    </div>
  </Card>

  <Card>
    <h3>🎯 What Happens When You Measure?</h3>
    
    <div class="measurement-process">
      <div class="process-step">
        <div class="step-number">1</div>
        <div class="step-content">
          <h4>Before Measurement: Superposition</h4>
          <p>The qubit exists in BOTH states at once - it's 0 AND 1 simultaneously!</p>
          <div class="visual-state superposition-visual">
            <div class="state-option">|0⟩</div>
            <div class="state-plus">+</div>
            <div class="state-option">|1⟩</div>
          </div>
        </div>
      </div>

      <div class="process-arrow">⬇️</div>

      <div class="process-step">
        <div class="step-number">2</div>
        <div class="step-content">
          <h4>During Measurement: Collapse</h4>
          <p>You observe the qubit - the superposition instantly collapses!</p>
          {#if quantumState === "measuring"}
            <div class="visual-state measuring-visual">
              <div class="collapse-animation">💥 COLLAPSING...</div>
            </div>
          {:else}
            <div class="visual-state">
              <div class="collapse-hint">👁️ Click "Measure Once" to see this happen</div>
            </div>
          {/if}
        </div>
      </div>

      <div class="process-arrow">⬇️</div>

      <div class="process-step">
        <div class="step-number">3</div>
        <div class="step-content">
          <h4>After Measurement: Definite State</h4>
          <p>The qubit is now EITHER 0 OR 1 - you get one specific answer!</p>
          {#if quantumState === "collapsed"}
            <div class="visual-state collapsed-visual" style="border-color: {currentStateInfo.color};">
              <div class="result-display" style="background: {currentStateInfo.color};">
                Result: {collapsedValue}
              </div>
              <div class="result-explanation">
                You measured <strong>|{collapsedValue}⟩</strong> with probability {percentages[collapsedValue]}%
              </div>
            </div>
          {:else}
            <div class="visual-state">
              <div class="waiting-result">? (Not measured yet)</div>
            </div>
          {/if}
        </div>
      </div>
    </div>

    <div class="key-insight">
      <strong>🔑 Key Point:</strong> You can't predict WHICH result you'll get (0 or 1), 
      but you CAN predict the PROBABILITY. That's quantum randomness!
    </div>
  </Card>

  <div class="controls">
    <button class="btn btn-primary" onclick={performMeasurement} disabled={isMeasuring}>
      {isMeasuring ? "⚡ Measuring..." : "🔬 Measure Once"}
    </button>
    <button class="btn btn-secondary" onclick={() => measureBatch(10)} disabled={isMeasuring}>
      📊 Measure 10x
    </button>
    <button class="btn btn-secondary" onclick={() => measureBatch(100)} disabled={isMeasuring}>
      📈 Measure 100x
    </button>
    <button class="btn btn-secondary" onclick={reset} disabled={isMeasuring || totalMeasurements === 0}>
      🔄 Reset
    </button>
  </div>

  {#if totalMeasurements > 0}
    <div class="stats">
      <h4>📊 Measurement Statistics</h4>
      <div class="stats-grid">
        <StatCard
          label="Result: 0"
          value={results["0"]}
          subtitle="{percentages['0']}%"
          variant="default"
        />
        <StatCard
          label="Result: 1"
          value={results["1"]}
          subtitle="{percentages['1']}%"
          variant="default"
        />
      </div>
      <p class="total-measurements">Total Measurements: {totalMeasurements}</p>
      
      <div class="stats-insight">
        <strong>📈 What This Means:</strong>
        <p>Expected with {currentBasisInfo.name}: <strong>{expectedDescription}</strong></p>
        <p>Your results: <strong>{percentages['0']}% zeros, {percentages['1']}% ones</strong></p>
        {#if selectedBasis === 'x' && (selectedState === 'definite_0' || selectedState === 'definite_1')}
          <p class="insight-warning">⚡ Measuring |{selectedState === 'definite_0' ? '0' : '1'}⟩ in X-basis gives 50-50! This is quantum basis incompatibility!</p>
        {:else if Math.abs(parseFloat(percentages['0']) - expectedProbs.prob0) < 15}
          <p class="insight-match">✅ Your results match the expected probability!</p>
        {:else if totalMeasurements < 50}
          <p class="insight-tip">💡 More measurements → Closer to expected probability</p>
        {/if}
      </div>
    </div>

    <div class="measurement-history">
      <h4>📜 Recent Measurements (Last 10)</h4>
      <div class="history-list">
        {#each measurements as measurement, i}
          <div class="history-item" style="animation-delay: {i * 0.05}s">
            <span class="measurement-result" style="background: {quantumStates[selectedState].color};">
              {measurement}
            </span>
          </div>
        {/each}
      </div>
    </div>
  {/if}

  <Card>
    <h3>🎁 Quantum Mystery Box</h3>
    <p>There's a magic box with balls inside - but you can't see inside! Pull out balls to guess what's in the box.</p>
    
    <div class="mystery-game">
      {#if !gameStarted}
        <div class="game-intro">
          <div class="box-visual">🎁</div>
          <p><strong>How to Play:</strong></p>
          <ol>
            <li>Click "Open Mystery Box" to start</li>
            <li>Pull out balls one by one (they're either 🔴 or 🔵)</li>
            <li>After 10 pulls, guess what's in the box!</li>
          </ol>
          <button class="btn btn-primary btn-large" onclick={startGame}>
            🎁 Open Mystery Box
          </button>
        </div>
      {:else}
        <div class="game-active">
          <div class="pulls-count">
            <span>Balls Pulled: {gamePulls}/10</span>
          </div>
          
          <div class="box-container">
            <div class="mystery-box">
              <div class="box-icon">📦</div>
              <div class="box-label">Mystery Box</div>
            </div>
            
            {#if gamePulls < 10}
              <button class="btn btn-primary pull-btn" onclick={pullBall} disabled={isMeasuring}>
                {isMeasuring ? '⚡ Pulling...' : '👋 Pull a Ball'}
              </button>
            {/if}
          </div>

          <div class="balls-pulled">
            <div class="balls-label">Balls you pulled:</div>
            <div class="balls-container">
              {#each gameBalls as ball}
                <span class="ball">{ball === '0' ? '🔴' : '🔵'}</span>
              {/each}
              {#each Array(10 - gamePulls) as _}
                <span class="ball empty">⚪</span>
              {/each}
            </div>
          </div>

          <div class="ball-stats">
            <div class="stat-item">
              <span class="ball-emoji">🔴</span>
              <span class="ball-count">{gameResults['0']}</span>
            </div>
            <div class="stat-item">
              <span class="ball-emoji">🔵</span>
              <span class="ball-count">{gameResults['1']}</span>
            </div>
          </div>

          {#if gamePulls >= 10 && !hasGuessed}
            <div class="guess-section">
              <h4>🤔 What do you think is in the box?</h4>
              <div class="simple-guess-buttons">
                <button class="simple-guess" onclick={() => makeSimpleGuess('equal')}>
                  <div class="guess-balls">🔴 🔵</div>
                  <div class="guess-label">50-50 Mix</div>
                  <div class="guess-detail">Half red, half blue</div>
                </button>
                <button class="simple-guess" onclick={() => makeSimpleGuess('biased_0')}>
                  <div class="guess-balls">🔴 🔴 🔴 🔵</div>
                  <div class="guess-label">Mostly Red</div>
                  <div class="guess-detail">75% red, 25% blue</div>
                </button>
                <button class="simple-guess" onclick={() => makeSimpleGuess('biased_1')}>
                  <div class="guess-balls">🔴 🔵 🔵 🔵</div>
                  <div class="guess-label">Mostly Blue</div>
                  <div class="guess-detail">25% red, 75% blue</div>
                </button>
                <button class="simple-guess" onclick={() => makeSimpleGuess('definite_0')}>
                  <div class="guess-balls">🔴 🔴 🔴</div>
                  <div class="guess-label">Only Red</div>
                  <div class="guess-detail">100% red balls</div>
                </button>
                <button class="simple-guess" onclick={() => makeSimpleGuess('definite_1')}>
                  <div class="guess-balls">🔵 🔵 🔵</div>
                  <div class="guess-label">Only Blue</div>
                  <div class="guess-detail">100% blue balls</div>
                </button>
              </div>
            </div>
          {/if}

          {#if showGameResult}
            <div class="game-result {gameCorrect ? 'win' : 'lose'}">
              <div class="result-emoji">{gameCorrect ? '🎉' : '😅'}</div>
              {#if gameCorrect}
                <h3>You Got It! 🎊</h3>
                <p>The box had: <strong>{gameStateNames[gameSecret]}</strong></p>
              {:else}
                <h3>Not Quite!</h3>
                <p>You guessed: <strong>{gameStateNames[gameGuess]}</strong></p>
                <p>But it was: <strong>{gameStateNames[gameSecret]}</strong></p>
              {/if}
              <button class="btn btn-primary" onclick={startGame}>
                🎮 Play Again
              </button>
            </div>
          {/if}
        </div>
      {/if}
    </div>
  </Card>
</div>