<script>
  import './stepContent.css';
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
      <Card variant="info">
        <p>
          In everyday life, things are either one way or another. A light is ON
          or OFF. A coin shows heads OR tails.
        </p>
        <p>
          But in the quantum world, things can be <strong
            >both at the same time</strong
          >!
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
        <h4>🔬 What You Can Do</h4>
        <p>
          <strong>Single Coin:</strong> 1 qubit with Hadamard gate → 50% heads, 50%
          tails
        </p>
        <p>
          <strong>Double Coin:</strong> 2 qubits with Hadamard gates → 25% each of
          4 outcomes
        </p>
        <p class="hint">
          Try running 100 measurements to see the probabilities converge to
          theoretical values!
        </p>
      </Card>

      <MultiCoinFlip />

      <Card variant="success" style="margin-top: 24px;">
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
