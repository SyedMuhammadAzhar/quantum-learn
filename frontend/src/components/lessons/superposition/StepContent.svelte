<script>
  import "./stepContent.css";
  // @ts-nocheck

  import { currentStep } from "../../../stores/lessonStore.js";
  import Card from "../../ui/Card.svelte";
  import QuantumCoinFlip from "../../quantum/QuantumCoinFlip.svelte";
  import FAQ from "./FAQ.svelte";
  import Quiz from "./Quiz.svelte";
  // @ts-ignore
  import MultiCoinFlip from "../../quantum/MultiCoinFlip.svelte";
</script>

<div class="step-content">
  {#if $currentStep?.id === "intro"}
    <div class="intro-step">
      <div class="big-emoji">🌌</div>
      <h1>Welcome to the Quantum World!</h1>
      <p class="lead">
        Get ready to explore one of the most mind-bending concepts in physics:
        <strong>Superposition</strong>.
      </p>

      <div class="what-youll-learn">
        <h3>🎯 What You'll Learn</h3>
        <div class="learn-items">
          <div class="learn-item">
            <span class="learn-icon">🪙</span>
            <p>
              How quantum "things" can be in <strong>two states at once</strong>
            </p>
          </div>
          <div class="learn-item">
            <span class="learn-icon">🖥️</span>
            <p>
              Why quantum computers are <strong>different</strong> from regular computers
            </p>
          </div>
          <div class="learn-item">
            <span class="learn-icon">🎮</span>
            <p>
              Play with a <strong>real quantum simulator</strong> to see it yourself!
            </p>
          </div>
        </div>
      </div>

      <Card variant="info">
        <h4>🤔 The Big Idea</h4>
        <p>In everyday life, things are either one way or another:</p>
        <div class="everyday-examples">
          <span>💡 Light is ON or OFF</span>
          <span>🚪 Door is OPEN or CLOSED</span>
          <span>🪙 Coin is HEADS or TAILS</span>
        </div>
        <p>
          But in the quantum world, things can be <strong
            >both at the same time</strong
          >! This is called <strong>Superposition</strong>.
        </p>
      </Card>

      <div class="fun-fact">
        <span class="fact-icon">🚀</span>
        <p>
          <strong>Why Should You Care?</strong> Quantum computers use this "both
          at once" trick to solve problems that would take regular computers millions
          of years! They could help discover new medicines, create unbreakable security,
          and solve climate change problems.
        </p>
      </div>

      <div class="no-math-promise">
        <span class="promise-icon">✨</span>
        <p>
          <strong>No complicated math needed!</strong> We'll explain everything with
          simple examples and fun animations.
        </p>
      </div>
    </div>
  {:else if $currentStep?.id === "classical"}
    <div class="classical-step">
      <h1>Classical vs Quantum</h1>
      <p class="lead">
        Let's see what makes quantum computers so special compared to regular
        computers.
      </p>

      <div class="simple-explanation">
        <Card variant="info">
          <h4>🤔 First, What is a "Bit"?</h4>
          <p>
            A <strong>bit</strong> is the smallest piece of information in a
            computer. It can only be one of two things: <strong>0</strong> or
            <strong>1</strong>.
          </p>
          <p class="analogy-text">
            Think of it like a light switch - it's either OFF (0) or ON (1).
            Nothing in between!
          </p>
        </Card>
      </div>

      <div class="comparison">
        <div class="comparison-card classical">
          <div class="card-header">🖥️ Regular Computer</div>
          <h3>Uses BITS</h3>
          <div class="bit-display">
            <div class="bit">0</div>
            <span class="or-text">OR</span>
            <div class="bit">1</div>
          </div>
          <div class="card-explanation">
            <p>✓ A bit is <strong>always</strong> either 0 or 1</p>
            <p>✓ Like a light switch: ON or OFF</p>
            <p>✓ Checks answers <strong>one at a time</strong></p>
          </div>
        </div>

        <div class="comparison-card quantum">
          <div class="card-header">⚛️ Quantum Computer</div>
          <h3>Uses QUBITS</h3>
          <div class="qubit-display">
            <div class="qubit spinning">0 & 1</div>
          </div>
          <div class="card-explanation">
            <p>✓ A qubit can be 0 <strong>AND</strong> 1 at the same time!</p>
            <p>✓ Like a spinning coin: both sides at once</p>
            <p>✓ Checks <strong>many answers simultaneously</strong></p>
          </div>
        </div>
      </div>

      <div class="power-example">
        <h4>💡 Why Is This So Powerful?</h4>
        <div class="power-comparison">
          <div class="power-item classical-power">
            <span class="power-label">Regular Computer</span>
            <p>
              Imagine searching for a name in a phone book with 1 million names.
            </p>
            <p class="power-result">
              Checks names <strong>one by one</strong> = Could take 1 million checks!
            </p>
          </div>
          <div class="power-item quantum-power">
            <span class="power-label">Quantum Computer</span>
            <p>The same phone book with 1 million names.</p>
            <p class="power-result">
              Checks <strong>many at once</strong> = Could take only ~1000 checks!
            </p>
          </div>
        </div>
      </div>

      <Card variant="success">
        <h4>🎯 Key Takeaway</h4>
        <p>
          The magic word is <strong>"AND"</strong> instead of
          <strong>"OR"</strong>. Regular bits are 0 OR 1. Quantum bits (qubits)
          are 0 AND 1. This lets quantum computers solve certain problems much,
          much faster!
        </p>
      </Card>
    </div>
  {:else if $currentStep?.id === "analogy"}
    <div class="analogy-step">
      <h1>The Spinning Coin 🪙</h1>
      <p class="lead">The best way to understand superposition.</p>

      <div class="coin-analogy">
        <div class="analogy-stage">
          <div class="stage-item">
            <div class="coin-static heads-up">H</div>
            <p><strong>Heads Up</strong></p>
            <p class="small">Definitely heads</p>
          </div>

          <div class="stage-item highlight">
            <div class="coin-spinning">
              <div class="spin-coin">?</div>
            </div>
            <p><strong>Spinning!</strong></p>
            <p class="small">Both heads AND tails!</p>
          </div>

          <div class="stage-item">
            <div class="coin-static tails-up">T</div>
            <p><strong>Tails Up</strong></p>
            <p class="small">Definitely tails</p>
          </div>
        </div>
      </div>

      <Card variant="info">
        <h4>🎯 Key Insight</h4>
        <p>
          When the coin is <strong>spinning</strong>, you can't say it's heads
          or tails. It's in a <strong>superposition</strong> of both states!
        </p>
        <p>
          Only when you <strong>catch it</strong> (measure it) does it become definitely
          one or the other.
        </p>
      </Card>

      <div class="important-difference">
        <h4>⚠️ Important: Quantum is NOT Just "Unknown"</h4>
        <p>
          When a regular coin is in your closed hand, it's <strong
            >definitely</strong
          > one side - you just don't know which.
        </p>
        <p>
          But a quantum coin in superposition is <strong>genuinely both</strong>
          at the same time! It only "picks a side" when you look at it. This is what
          makes quantum so strange and powerful.
        </p>
      </div>

      <div class="quantum-connection">
        <h4>In Quantum Terms:</h4>
        <ul>
          <li>🪙 Spinning coin = Qubit in superposition</li>
          <li>✋ Catching the coin = Measuring the qubit</li>
          <li>👀 Seeing heads or tails = Getting 0 or 1</li>
        </ul>
      </div>
    </div>
  {:else if $currentStep?.id === "math"}
    <div class="math-step">
      <h1>The Math (Made Simple) 📐</h1>
      <p class="lead">Don't worry, we'll keep it friendly!</p>

      <Card>
        <h4>Quantum State Notation</h4>
        <div class="notation">
          <div class="state-box">
            <span class="ket">|0⟩</span>
            <p>Read as "ket zero"</p>
            <p class="small">Like saying "Heads"</p>
          </div>
          <div class="state-box">
            <span class="ket">|1⟩</span>
            <p>Read as "ket one"</p>
            <p class="small">Like saying "Tails"</p>
          </div>
        </div>
      </Card>

      <Card variant="info">
        <h4>Superposition State</h4>
        <div class="superposition-formula">
          <span class="formula">|ψ⟩ = α|0⟩ + β|1⟩</span>
        </div>
        <p>
          This means: "The qubit is <strong>partly</strong> in state 0 and
          <strong>partly</strong> in state 1 at the same time."
        </p>
        <p>
          α and β tell us the <strong>probability</strong> of measuring each state.
        </p>
      </Card>

      <Card variant="success">
        <h4>🎲 The Hadamard Gate</h4>
        <p>
          This is the magic operation that creates a <strong
            >50/50 superposition</strong
          >:
        </p>
        <div class="hadamard-visual">
          <span class="ket">|0⟩</span>
          <span class="arrow">→ H →</span>
          <span class="formula-small">(|0⟩ + |1⟩)/√2</span>
        </div>
        <p>
          It turns a definite 0 into an <strong>equal mix</strong> of 0 and 1.
        </p>
        <p class="small">
          (The √2 is just to make the math work out - it ensures probabilities
          add to 100%)
        </p>
      </Card>
    </div>
  {:else if $currentStep?.id === "demo"}
    <div class="demo-step">
      <h1>Try It Yourself! 🎮</h1>
      <p class="lead">
        Now put your knowledge to the test with real quantum simulations powered
        by Qiskit!
      </p>

      <Card variant="info">
        <h4>🎯 How to Use This Demo</h4>
        <div class="demo-instructions">
          <div class="instruction-step">
            <span class="step-number">1</span>
            <p>
              <strong>Choose Single or Double Coin</strong> - Start with single to
              understand the basics
            </p>
          </div>
          <div class="instruction-step">
            <span class="step-number">2</span>
            <p>
              <strong>Click "Measure"</strong> - Watch the quantum coin collapse
              from superposition to a definite state
            </p>
          </div>
          <div class="instruction-step">
            <span class="step-number">3</span>
            <p>
              <strong>Run 100 Measurements</strong> - See how probabilities converge
              to ~50/50 over many trials!
            </p>
          </div>
        </div>
        <p class="hint">
          💡 Notice: Each measurement is truly random - quantum randomness, not
          pseudo-random like regular computers!
        </p>
      </Card>

      <MultiCoinFlip />

      <div class="why-matters">
        <h4>🚀 Why This Matters</h4>
        <div class="matters-grid">
          <div class="matters-item">
            <span class="matters-icon">💊</span>
            <div>
              <strong>Drug Discovery</strong>
              <p>Simulate molecules to find new medicines faster</p>
            </div>
          </div>
          <div class="matters-item">
            <span class="matters-icon">🔐</span>
            <div>
              <strong>Cryptography</strong>
              <p>Create unbreakable encryption for secure communications</p>
            </div>
          </div>
          <div class="matters-item">
            <span class="matters-icon">🧠</span>
            <div>
              <strong>AI & Machine Learning</strong>
              <p>Train AI models exponentially faster</p>
            </div>
          </div>
          <div class="matters-item">
            <span class="matters-icon">📦</span>
            <div>
              <strong>Optimization</strong>
              <p>Find the best routes, schedules, and solutions</p>
            </div>
          </div>
        </div>
      </div>

      <Card variant="success">
        <h4>What Did You Learn?</h4>
        <ul class="learn-list">
          <li>
            <strong>Single Coin (1 qubit):</strong>
            50% heads, 50% tails - true quantum randomness from superposition
          </li>
          <li>
            <strong>Double Coin (2 qubits):</strong>
            25% each outcome - quantum states grow exponentially!
          </li>
          <li>
            <strong>Key Point:</strong>
            N qubits = 2ᴺ possible states. That's why quantum computers are powerful!
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
