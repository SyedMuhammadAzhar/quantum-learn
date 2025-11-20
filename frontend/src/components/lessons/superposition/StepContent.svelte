<script>
  import { currentStep } from "../../../stores/lessonStore.js";
  import Card from "../../ui/Card.svelte";
  import QuantumCoinFlip from "../../quantum/QuantumCoinFlip.svelte";
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
      <Card variant="info">
        <p>
          In everyday life, things are either one way or another. A light is ON
          or OFF. A coin shows heads OR tails.
        </p>
        <p>
          But in the quantum world, things can be <strong
            >both at the same time</strong
          >! 🤯
        </p>
      </Card>
      <div class="fun-fact">
        <span class="fact-icon">💡</span>
        <p>
          <strong>Fun Fact:</strong> Quantum computers use this "both at once" trick
          to solve problems that would take regular computers millions of years!
        </p>
      </div>
    </div>
  {:else if $currentStep?.id === "classical"}
    <div class="classical-step">
      <h1>Classical vs Quantum</h1>
      <p class="lead">Let's see what makes quantum so special.</p>

      <div class="comparison">
        <div class="comparison-card classical">
          <h3>🖥️ Classical Computer</h3>
          <div class="bit-display">
            <div class="bit">0</div>
            <span>OR</span>
            <div class="bit">1</div>
          </div>
          <p>A bit is always 0 <strong>or</strong> 1. Never both.</p>
          <p>Like a light switch: ON or OFF.</p>
        </div>

        <div class="comparison-card quantum">
          <h3>⚛️ Quantum Computer</h3>
          <div class="qubit-display">
            <div class="qubit spinning">0 & 1</div>
          </div>
          <p>A qubit can be 0 <strong>and</strong> 1 simultaneously!</p>
          <p>Like a spinning coin: both sides at once.</p>
        </div>
      </div>

      <Card>
        <p>
          <strong>Why does this matter?</strong> Because while a classical computer
          checks possibilities one by one, a quantum computer can explore many possibilities
          at once!
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

          <div class="stage-item">
            <div class="coin-spinning">
              <div class="spin-coin">?</div>
            </div>
            <p><strong>Spinning</strong></p>
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
        Now put your knowledge to the test with a real quantum simulation!
      </p>

      <Card variant="info">
        <p>
          <strong>What you're about to do:</strong> You'll flip a quantum coin
          that's powered by a real quantum circuit simulation using
          <strong>Qiskit</strong>
          (IBM's quantum computing library).
        </p>
      </Card>

      <QuantumCoinFlip />
    </div>
  {/if}
</div>

<style>
  .step-content {
    animation: fadeIn 0.5s ease;
  }

  @keyframes fadeIn {
    from {
      opacity: 0;
      transform: translateY(10px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  h1 {
    color: var(--color-text-primary);
    margin-bottom: var(--spacing-md);
  }

  .lead {
    font-size: var(--font-size-lg);
    color: var(--color-text-secondary);
    margin-bottom: var(--spacing-lg);
  }

  .big-emoji {
    font-size: 80px;
    text-align: center;
    margin-bottom: var(--spacing-lg);
  }

  .fun-fact {
    background: linear-gradient(135deg, #ffecd2, #fcb69f);
    padding: var(--spacing-lg);
    border-radius: var(--radius-lg);
    display: flex;
    align-items: flex-start;
    gap: var(--spacing-md);
    margin-top: var(--spacing-lg);
  }

  .fact-icon {
    font-size: 32px;
  }

  .fun-fact p {
    margin: 0;
  }

  /* Classical vs Quantum */
  .comparison {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: var(--spacing-lg);
    margin-bottom: var(--spacing-lg);
  }

  .comparison-card {
    background: var(--color-surface);
    padding: var(--spacing-lg);
    border-radius: var(--radius-lg);
    text-align: center;
    box-shadow: var(--shadow-sm);
  }

  .comparison-card h3 {
    margin-top: 0;
  }

  .bit-display {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: var(--spacing-md);
    margin: var(--spacing-lg) 0;
  }

  .bit {
    width: 60px;
    height: 60px;
    background: var(--color-border);
    border-radius: var(--radius-md);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: var(--font-size-2xl);
    font-weight: bold;
  }

  .qubit-display {
    margin: var(--spacing-lg) 0;
  }

  .qubit {
    width: 80px;
    height: 80px;
    background: linear-gradient(
      135deg,
      var(--color-primary),
      var(--color-purple)
    );
    border-radius: 50%;
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: bold;
  }

  .qubit.spinning {
    animation: spin 2s linear infinite;
  }

  @keyframes spin {
    from {
      transform: rotate(0deg);
    }
    to {
      transform: rotate(360deg);
    }
  }

  /* Coin Analogy */
  .analogy-stage {
    display: flex;
    justify-content: space-around;
    align-items: center;
    background: var(--color-surface);
    padding: var(--spacing-xl);
    border-radius: var(--radius-lg);
    margin-bottom: var(--spacing-lg);
  }

  .stage-item {
    text-align: center;
  }

  .coin-static {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: var(--font-size-2xl);
    font-weight: bold;
    color: white;
    margin: 0 auto var(--spacing-sm);
  }

  .heads-up {
    background: var(--color-heads);
  }

  .tails-up {
    background: var(--color-tails);
  }

  .coin-spinning {
    width: 80px;
    height: 80px;
    margin: 0 auto var(--spacing-sm);
  }

  .spin-coin {
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, var(--color-heads), var(--color-tails));
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: var(--font-size-2xl);
    font-weight: bold;
    color: white;
    animation: spinY 0.8s linear infinite;
  }

  @keyframes spinY {
    from {
      transform: rotateY(0deg);
    }
    to {
      transform: rotateY(360deg);
    }
  }

  .small {
    font-size: var(--font-size-sm);
    color: var(--color-text-muted);
  }

  .quantum-connection {
    background: var(--color-surface);
    padding: var(--spacing-lg);
    border-radius: var(--radius-lg);
  }

  .quantum-connection ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .quantum-connection li {
    padding: var(--spacing-sm) 0;
    font-size: var(--font-size-base);
  }

  /* Math Step */
  .notation {
    display: flex;
    justify-content: center;
    gap: var(--spacing-xl);
    margin: var(--spacing-lg) 0;
  }

  .state-box {
    text-align: center;
  }

  .ket {
    font-size: var(--font-size-3xl);
    font-family: "Times New Roman", serif;
    color: var(--color-primary);
  }

  .superposition-formula {
    text-align: center;
    margin: var(--spacing-lg) 0;
  }

  .formula {
    font-size: var(--font-size-2xl);
    font-family: "Times New Roman", serif;
    color: var(--color-primary);
  }

  .hadamard-visual {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: var(--spacing-md);
    margin: var(--spacing-lg) 0;
    font-size: var(--font-size-xl);
  }

  .arrow {
    color: var(--color-success);
    font-weight: bold;
  }

  .formula-small {
    font-family: "Times New Roman", serif;
    color: var(--color-primary);
  }

  /* Demo Step */
  .demo-step {
    /* Demo component has its own styling */
  }
</style>
