<script>
  import './stepContent.css';
  // @ts-nocheck

  import { currentStep } from "../../../stores/lessonStore.js";
  import Card from "../../ui/Card.svelte";
  import FAQ from "./FAQ.svelte";
  import Quiz from "./Quiz.svelte";
  import MeasurementDemo from "../../quantum/MeasurementDemo.svelte";
</script>

<div class="step-content">
  {#if $currentStep?.id === "intro"}
    <div class="intro-step">
      <div class="big-emoji">👁️</div>
      <h1>Welcome to Quantum Measurement!</h1>
      <p class="lead">
        Prepare to explore the most mysterious aspect of quantum mechanics:
        <strong>How observation changes reality</strong>.
      </p>
      <Card variant="info">
        <p>
          In the classical world, measuring something doesn't change it. You can
          check the temperature, weigh an apple, or measure a distance without
          affecting them.
        </p>
        <p>
          But in the quantum world, <strong>the act of measurement fundamentally
          changes what you're measuring</strong>! This is called wavefunction collapse.
        </p>
      </Card>
      <div class="fun-fact">
        <span class="fact-icon">🎭</span>
        <p>
          <strong>Fun Fact:</strong> The famous thought experiment "Schrödinger's
          Cat" was created to show how bizarre quantum measurement is - a cat that's
          both alive AND dead until you look!
        </p>
      </div>
    </div>
  {:else if $currentStep?.id === "what-happens"}
    <div class="what-happens-step">
      <h1>What Happens When You Measure? 📊</h1>
      <p class="lead">Measurement is the moment quantum weirdness becomes classical reality.</p>

      <div class="measurement-journey">
        <div class="journey-step">
          <div class="journey-icon before-icon">🌊</div>
          <div class="journey-content">
            <h3>Before Measurement</h3>
            <div class="state-visual superposition-state">
              <div class="spinning-coin">🪙</div>
              <div class="state-formula">|ψ⟩ = α|0⟩ + β|1⟩</div>
            </div>
            <p class="state-description">
              <strong>Superposition:</strong> The qubit exists in BOTH states at once!
            </p>
            <p class="analogy">🪙 Like a coin spinning in the air - it's neither heads nor tails yet.</p>
          </div>
        </div>

        <div class="journey-arrow">
          <div class="arrow-line"></div>
          <div class="arrow-label">👁️ You Look!</div>
          <div class="arrow-line"></div>
        </div>

        <div class="journey-step">
          <div class="journey-icon during-icon">💥</div>
          <div class="journey-content">
            <h3>During Measurement</h3>
            <div class="state-visual collapse-state">
              <div class="collapse-animation-visual">
                <span class="collapse-wave">〰️</span>
                <span class="collapse-bang">💥</span>
                <span class="collapse-wave">〰️</span>
              </div>
              <div class="collapse-text">WAVEFUNCTION COLLAPSE!</div>
            </div>
            <p class="state-description">
              <strong>Collapse:</strong> The moment you observe, superposition vanishes instantly!
            </p>
            <p class="analogy">🖐️ Like catching the coin - NOW it must choose!</p>
          </div>
        </div>

        <div class="journey-arrow">
          <div class="arrow-line"></div>
          <div class="arrow-label">⚡ Instant!</div>
          <div class="arrow-line"></div>
        </div>

        <div class="journey-step">
          <div class="journey-icon after-icon">🎯</div>
          <div class="journey-content">
            <h3>After Measurement</h3>
            <div class="state-visual result-state">
              <div class="result-options">
                <div class="result-option">
                  <div class="result-circle result-0">0</div>
                  <span>|0⟩</span>
                </div>
                <div class="result-or">OR</div>
                <div class="result-option">
                  <div class="result-circle result-1">1</div>
                  <span>|1⟩</span>
                </div>
              </div>
            </div>
            <p class="state-description">
              <strong>Definite State:</strong> Now it's EITHER 0 OR 1 - one specific answer!
            </p>
            <p class="analogy">🪙 The coin landed - it's definitely heads or definitely tails.</p>
          </div>
        </div>
      </div>

      <div class="warning-card">
        <div class="warning-icon">⚠️</div>
        <div class="warning-content">
          <h4>Measurement is Irreversible!</h4>
          <p>Once you measure, you can <strong>NEVER</strong> get the superposition back.</p>
          <div class="warning-visual">
            <span class="no-return">|0⟩+|1⟩</span>
            <span class="arrow-forward">→ Measure →</span>
            <span class="final-state">|0⟩</span>
            <span class="no-arrow">✗ Can't go back!</span>
          </div>
          <p class="warning-detail">
            The quantum information is destroyed forever. This is why quantum computers
            must be so careful about when they measure!
          </p>
        </div>
      </div>

      <div class="key-points">
        <h4>🔑 Key Points About Measurement:</h4>
        <div class="points-grid">
          <div class="point-item">
            <span class="point-icon">🎲</span>
            <div class="point-text">
              <strong>Random outcome</strong>
              <p>You can't predict which result you'll get</p>
            </div>
          </div>
          <div class="point-item">
            <span class="point-icon">📊</span>
            <div class="point-text">
              <strong>Probabilistic</strong>
              <p>Quantum mechanics only tells you the odds</p>
            </div>
          </div>
          <div class="point-item">
            <span class="point-icon">⚡</span>
            <div class="point-text">
              <strong>Instantaneous</strong>
              <p>Collapse happens the exact moment you measure</p>
            </div>
          </div>
          <div class="point-item">
            <span class="point-icon">🚫</span>
            <div class="point-text">
              <strong>Irreversible</strong>
              <p>You can never recover the original superposition</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  {:else if $currentStep?.id === "born-rule"}
    <div class="born-rule-step">
      <h1>The Born Rule 📐</h1>
      <p class="lead">
        How to calculate the probability of getting each measurement result.
      </p>

      <Card>
        <h4>Quantum State Notation</h4>
        <div class="state-notation">
          <div class="formula-box">
            <span class="formula-large">|ψ⟩ = α|0⟩ + β|1⟩</span>
          </div>
          <p>Where:</p>
          <ul class="notation-list">
            <li><strong>α</strong> (alpha) = probability amplitude for state |0⟩</li>
            <li><strong>β</strong> (beta) = probability amplitude for state |1⟩</li>
            <li><strong>|α|² + |β|² = 1</strong> (probabilities must add to 100%)</li>
          </ul>
        </div>
      </Card>

      <Card variant="info">
        <h4>🎯 The Born Rule</h4>
        <div class="born-rule-formula">
          <p class="rule-text">
            The probability of measuring a particular outcome is the <strong>square
            of the amplitude</strong>:
          </p>
          <div class="formula-box">
            <span class="formula-large">P(0) = |α|²</span>
            <span class="spacing">and</span>
            <span class="formula-large">P(1) = |β|²</span>
          </div>
        </div>
      </Card>

      <div class="examples-section">
        <h4>📝 Examples:</h4>
        
        <div class="example-card">
          <h5>Example 1: Equal Superposition</h5>
          <div class="example-content">
            <p class="formula">|ψ⟩ = (|0⟩ + |1⟩)/√2</p>
            <p>Here: α = 1/√2, β = 1/√2</p>
            <p class="calculation">
              P(0) = |1/√2|² = 1/2 = <strong>50%</strong><br/>
              P(1) = |1/√2|² = 1/2 = <strong>50%</strong>
            </p>
            <p class="result">Equal chance of getting 0 or 1!</p>
          </div>
        </div>

        <div class="example-card">
          <h5>Example 2: Biased State</h5>
          <div class="example-content">
            <p class="formula">|ψ⟩ = (√3|0⟩ + |1⟩)/2</p>
            <p>Here: α = √3/2, β = 1/2</p>
            <p class="calculation">
              P(0) = |√3/2|² = 3/4 = <strong>75%</strong><br/>
              P(1) = |1/2|² = 1/4 = <strong>25%</strong>
            </p>
            <p class="result">More likely to get 0 than 1!</p>
          </div>
        </div>
      </div>
    </div>
  {:else if $currentStep?.id === "measurement-bases"}
    <div class="bases-step">
      <h1>Measurement Bases 🧭</h1>
      <p class="lead">
        The way you measure determines what answers you can get!
      </p>

      <div class="bases-intro">
        <div class="intro-visual">
          <span class="question-mark">❓</span>
        </div>
        <div class="intro-text">
          <h4>What is a Measurement Basis?</h4>
          <p>
            Imagine asking a question about a color. You could ask:
          </p>
          <ul class="analogy-list">
            <li><strong>"Is it red or blue?"</strong> → One type of answer</li>
            <li><strong>"Is it light or dark?"</strong> → A completely different answer!</li>
          </ul>
          <p>
            A measurement basis is like choosing <em>which question to ask</em> your qubit.
            Different questions → Different possible answers!
          </p>
        </div>
      </div>

      <div class="bases-comparison">
        <div class="basis-card-improved z-basis">
          <div class="basis-header">
            <span class="basis-emoji">📊</span>
            <h4>Z-Basis (Computational)</h4>
          </div>
          <div class="basis-question">
            <span class="question-label">Question:</span>
            <span class="question-text">"Is it 0 or 1?"</span>
          </div>
          <div class="basis-answers">
            <div class="answer-option">
              <div class="answer-circle z-0">0</div>
              <span class="answer-state">|0⟩</span>
            </div>
            <span class="answer-or">or</span>
            <div class="answer-option">
              <div class="answer-circle z-1">1</div>
              <span class="answer-state">|1⟩</span>
            </div>
          </div>
          <div class="basis-usage">
            <span class="usage-icon">💻</span>
            <p>This is the standard basis - what computers use for bits!</p>
          </div>
          <div class="basis-diagram">
            <div class="diagram-vertical">
              <span class="diagram-top">|0⟩ ↑</span>
              <div class="diagram-line vertical"></div>
              <span class="diagram-bottom">↓ |1⟩</span>
            </div>
          </div>
        </div>

        <div class="basis-card-improved x-basis">
          <div class="basis-header">
            <span class="basis-emoji">✖️</span>
            <h4>X-Basis (Hadamard)</h4>
          </div>
          <div class="basis-question">
            <span class="question-label">Question:</span>
            <span class="question-text">"Is it + or −?"</span>
          </div>
          <div class="basis-answers">
            <div class="answer-option">
              <div class="answer-circle x-plus">+</div>
              <span class="answer-state">|+⟩</span>
            </div>
            <span class="answer-or">or</span>
            <div class="answer-option">
              <div class="answer-circle x-minus">−</div>
              <span class="answer-state">|−⟩</span>
            </div>
          </div>
          <div class="basis-usage">
            <span class="usage-icon">🔐</span>
            <p>Used in quantum cryptography and creating superpositions!</p>
          </div>
          <div class="basis-diagram">
            <div class="diagram-horizontal">
              <span class="diagram-left">|−⟩ ←</span>
              <div class="diagram-line horizontal"></div>
              <span class="diagram-right">→ |+⟩</span>
            </div>
          </div>
        </div>
      </div>

      <div class="mind-blowing">
        <div class="mind-icon">🤯</div>
        <div class="mind-content">
          <h4>Here's the Mind-Blowing Part!</h4>
          <p>The SAME qubit gives DIFFERENT results depending on which basis you measure in:</p>
          
          <div class="example-comparison">
            <div class="example-box">
              <h5>Example: Qubit in state |0⟩</h5>
              <div class="example-results">
                <div class="example-result">
                  <span class="measure-basis">Z-Basis:</span>
                  <span class="measure-outcome certain">Always 0 ✓</span>
                </div>
                <div class="example-result">
                  <span class="measure-basis">X-Basis:</span>
                  <span class="measure-outcome random">50% + or − 🎲</span>
                </div>
              </div>
            </div>
            
            <div class="example-box">
              <h5>Example: Qubit in state |+⟩</h5>
              <div class="example-results">
                <div class="example-result">
                  <span class="measure-basis">Z-Basis:</span>
                  <span class="measure-outcome random">50% 0 or 1 🎲</span>
                </div>
                <div class="example-result">
                  <span class="measure-basis">X-Basis:</span>
                  <span class="measure-outcome certain">Always + ✓</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <Card variant="success">
        <h4>🔑 Why This Matters</h4>
        <p>
          <strong>Quantum cryptography</strong> uses this! Alice can encode information 
          in different bases. If an eavesdropper (Eve) measures in the wrong basis, 
          she gets random garbage instead of the message!
        </p>
        <p>
          This is why quantum communication is theoretically unhackable - measuring 
          disturbs the quantum state, and wrong-basis measurement reveals nothing useful!
        </p>
      </Card>
    </div>
  {:else if $currentStep?.id === "schrodinger"}
    <div class="schrodinger-step">
      <h1>Schrödinger's Cat 🐱📦</h1>
      <p class="lead">
        The most famous thought experiment in quantum mechanics - and it's weirder than you think!
      </p>

      <div class="story-intro">
        <div class="story-year">
          <span class="year">1935</span>
          <span class="location">Austria</span>
        </div>
        <div class="story-text">
          <p>
            Physicist <strong>Erwin Schrödinger</strong> was frustrated with quantum mechanics. 
            To show how bizarre the theory was, he imagined a diabolical experiment...
          </p>
        </div>
      </div>

      <div class="experiment-container">
        <h3>🔬 The Thought Experiment</h3>
        
        <div class="setup-cards">
          <div class="setup-item">
            <div class="setup-icon">📦</div>
            <div class="setup-text">
              <strong>A sealed box</strong>
              <p>Completely isolated - no one can see inside</p>
            </div>
          </div>
          <div class="setup-item">
            <div class="setup-icon">🐱</div>
            <div class="setup-text">
              <strong>A cat</strong>
              <p>Placed inside the box (don't worry, it's imaginary!)</p>
            </div>
          </div>
          <div class="setup-item">
            <div class="setup-icon">☢️</div>
            <div class="setup-text">
              <strong>A radioactive atom</strong>
              <p>50% chance to decay in 1 hour</p>
            </div>
          </div>
          <div class="setup-item">
            <div class="setup-icon">⚗️</div>
            <div class="setup-text">
              <strong>A poison vial</strong>
              <p>Breaks if atom decays → cat dies</p>
            </div>
          </div>
        </div>

        <div class="the-box">
          <div class="box-visual">
            <div class="box-outer">
              <div class="box-mystery">
                <span class="mystery-cat">🐱</span>
                <span class="mystery-question">❓</span>
              </div>
              <div class="box-chain">
                <span>☢️</span>
                <span class="chain-arrow">→</span>
                <span>⚗️</span>
                <span class="chain-arrow">→</span>
                <span>💀?</span>
              </div>
            </div>
            <div class="box-label-tag">SEALED - DO NOT OPEN</div>
          </div>
        </div>
      </div>

      <div class="paradox-section">
        <div class="paradox-header">
          <span class="paradox-icon">🤯</span>
          <h3>The Quantum Paradox</h3>
        </div>
        
        <div class="paradox-content">
          <div class="quantum-logic">
            <div class="logic-step">
              <div class="step-num">1</div>
              <div class="step-content">
                <p>The radioactive atom is in <strong>superposition</strong>:</p>
                <div class="formula-display atom-formula">
                  |atom⟩ = |decayed⟩ + |not decayed⟩
                </div>
              </div>
            </div>
            
            <div class="logic-arrow">⬇️</div>
            
            <div class="logic-step">
              <div class="step-num">2</div>
              <div class="step-content">
                <p>The atom's state is <strong>entangled</strong> with the cat:</p>
                <div class="formula-display entangled-formula">
                  |decayed⟩ → 💀 Dead cat<br/>
                  |not decayed⟩ → 🐱 Alive cat
                </div>
              </div>
            </div>
            
            <div class="logic-arrow">⬇️</div>
            
            <div class="logic-step highlight-step">
              <div class="step-num">3</div>
              <div class="step-content">
                <p>Therefore, the cat is ALSO in <strong>superposition</strong>:</p>
                <div class="formula-display cat-formula">
                  |cat⟩ = |alive⟩ + |dead⟩
                </div>
                <p class="shocking">The cat is <span class="both">ALIVE</span> and <span class="both">DEAD</span> at the same time!</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="measurement-moment">
        <h3>👁️ The Moment of Truth</h3>
        <p>What happens when you open the box?</p>
        
        <div class="open-box-visual">
          <div class="box-state before-state">
            <div class="state-label">Before Opening</div>
            <div class="cat-state superposed">
              <span class="ghost-cat alive-ghost">🐱</span>
              <span class="plus-sign">+</span>
              <span class="ghost-cat dead-ghost">💀</span>
            </div>
            <p>Both states exist simultaneously</p>
          </div>
          
          <div class="open-action">
            <div class="eye-icon">👁️</div>
            <div class="action-text">YOU LOOK!</div>
            <div class="collapse-burst">💥</div>
          </div>
          
          <div class="box-state after-state">
            <div class="state-label">After Opening</div>
            <div class="cat-state collapsed">
              <div class="outcome-option">
                <span class="outcome-cat">🐱💚</span>
                <span class="outcome-label">Alive!</span>
              </div>
              <div class="outcome-or">OR</div>
              <div class="outcome-option">
                <span class="outcome-cat">😿💀</span>
                <span class="outcome-label">Dead</span>
              </div>
            </div>
            <p>Only ONE outcome - 50% chance each</p>
          </div>
        </div>
      </div>

      <div class="schrodinger-point">
        <div class="point-header">
          <span class="point-icon">💡</span>
          <h3>What Was Schrödinger's Point?</h3>
        </div>
        <div class="point-content">
          <p>
            Here's the twist: <strong>Schrödinger wasn't celebrating quantum mechanics - he was criticizing it!</strong>
          </p>
          <div class="point-cards">
            <div class="point-card criticism">
              <h4>His Criticism</h4>
              <p>
                "Look how absurd this theory is! It says a cat can be alive AND dead. 
                That's clearly ridiculous - something must be wrong with quantum mechanics!"
              </p>
            </div>
            <div class="point-card reality">
              <h4>The Reality</h4>
              <p>
                Experiments have shown that quantum superposition IS real at small scales. 
                The question remains: why don't we see it at large scales like cats?
              </p>
            </div>
          </div>
        </div>
      </div>

      <div class="mystery-questions">
        <h3>🔮 The Measurement Problem</h3>
        <p>Questions physicists STILL debate today:</p>
        <div class="questions-grid">
          <div class="question-card">
            <span class="q-icon">⏱️</span>
            <p><strong>When</strong> exactly does superposition collapse?</p>
          </div>
          <div class="question-card">
            <span class="q-icon">🎯</span>
            <p><strong>What</strong> counts as a "measurement"?</p>
          </div>
          <div class="question-card">
            <span class="q-icon">👁️</span>
            <p>Does <strong>consciousness</strong> play a role?</p>
          </div>
          <div class="question-card">
            <span class="q-icon">🌌</span>
            <p>Do <strong>parallel universes</strong> exist where the cat is alive AND dead?</p>
          </div>
        </div>
      </div>

      <div class="fun-facts-section">
        <h3>🎉 Fun Facts</h3>
        <div class="fun-facts-grid">
          <div class="fun-fact-card">
            <span class="fact-emoji">🎬</span>
            <p>Schrödinger's cat appears in TV shows (Big Bang Theory), movies, and video games!</p>
          </div>
          <div class="fun-fact-card">
            <span class="fact-emoji">🔬</span>
            <p>Scientists have created "Schrödinger's cats" with molecules - not actual cats, but particles in superposition!</p>
          </div>
          <div class="fun-fact-card">
            <span class="fact-emoji">😅</span>
            <p>Schrödinger reportedly said he wished he'd never met that cat!</p>
          </div>
        </div>
      </div>
    </div>
  {:else if $currentStep?.id === "demo"}
    <div class="demo-step">
      <h1>Try It Yourself! 🎮</h1>
      <p class="lead">
        Experiment with quantum measurement and see wavefunction collapse in action!
      </p>

      <Card variant="info">
        <h4>🔬 What You Can Do</h4>
        <p>
          <strong>Prepare quantum states:</strong> Create different superposition states
        </p>
        <p>
          <strong>Choose measurement basis:</strong> Z-basis (computational) or X-basis (Hadamard)
        </p>
        <p>
          <strong>Measure & observe collapse:</strong> Watch probabilities become definite results!
        </p>
        <p class="hint">
          Try measuring the same state in different bases to see how results change!
        </p>
      </Card>

      <MeasurementDemo />

      <Card variant="success" style={"margin-top: 24px;"}>
        <h4>What Did You Learn?</h4>
        <ul class="learn-list">
          <li>
            <strong>Superposition → Measurement → Collapse:</strong>
            Quantum states exist in superposition until measured
          </li>
          <li>
            <strong>Born Rule works:</strong>
            Probabilities match |amplitude|² after many measurements
          </li>
          <li>
            <strong>Basis matters:</strong>
            Different bases give different measurement outcomes
          </li>
          <li>
            <strong>Randomness is real:</strong>
            You can't predict individual outcomes, only probabilities!
          </li>
        </ul>
      </Card>
    </div>
  {:else if $currentStep?.id === "faq"}
    <FAQ />
  {:else if $currentStep?.id === "quiz"}
    <Quiz />
  {/if}
</div>