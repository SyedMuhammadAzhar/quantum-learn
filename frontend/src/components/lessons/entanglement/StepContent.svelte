<script>
  import './stepContent.css';
  // @ts-nocheck

  import { currentStep } from "../../../stores/lessonStore.js";
  import Card from "../../ui/Card.svelte";
  import FAQ from "./FAQ.svelte";
  import Quiz from "./Quiz.svelte";
  import EntanglementDemo from "../../quantum/EntanglementDemo.svelte";
</script>

<div class="step-content">
  {#if $currentStep?.id === "intro"}
    <div class="intro-step">
      <div class="big-emoji">🔗</div>
      <h1>Welcome to Quantum Entanglement!</h1>
      <p class="lead">
        Prepare to explore what Einstein called
        <strong>"spooky action at a distance"</strong> - one of the most
        fascinating phenomena in quantum physics.
      </p>
      <Card variant="info">
        <p>
          Imagine two particles that are mysteriously connected, no matter how
          far apart they are. Measure one, and you instantly know something
          about the other - even if it's on the other side of the universe!
        </p>
        <p>
          This isn't science fiction. This is <strong
            >quantum entanglement</strong
          >, and it's real.
        </p>
      </Card>
      <div class="fun-fact">
        <span class="fact-icon">🌟</span>
        <p>
          <strong>Fun Fact:</strong> Quantum entanglement is being used today for
          ultra-secure communication and will be crucial for quantum internet and
          quantum teleportation!
        </p>
      </div>
    </div>
  {:else if $currentStep?.id === "what-is"}
    <div class="what-is-step">
      <h1>What is Entanglement? 🤝</h1>
      <p class="lead">
        Entanglement is a special quantum connection between particles.
      </p>

      <div class="comparison">
        <div class="comparison-card classical">
          <h3>👯 Classical Correlation</h3>
          <div class="classical-visual">
            <div class="particle">👟</div>
            <div class="particle">👟</div>
          </div>
          <p>
            Like a pair of shoes in separate boxes. If you open one box and
            find a left shoe, you know the other box has the right shoe.
          </p>
          <p><strong>The correlation existed before you looked.</strong></p>
        </div>

        <div class="comparison-card quantum">
          <h3>⚛️ Quantum Entanglement</h3>
          <div class="quantum-visual">
            <div class="particle-container">
              <div class="entangled-particle pulse">?</div>
              <div class="particle-label">Particle A<br/><small>Superposition</small></div>
            </div>
            <div class="connection-line"></div>
            <div class="particle-container">
              <div class="entangled-particle pulse">?</div>
              <div class="particle-label">Particle B<br/><small>Superposition</small></div>
            </div>
          </div>
          <p>
            Entangled particles don't have definite states until measured.
            When you measure one, it instantly affects the other!
          </p>
          <p><strong>The correlation is created by the measurement.</strong></p>
        </div>
      </div>

      <Card variant="success">
        <h4>🎯 Key Point</h4>
        <p>
          With entanglement, the particles share a quantum state. They're not
          just correlated - they're part of the same quantum system, even when
          separated by vast distances.
        </p>
      </Card>
    </div>
  {:else if $currentStep?.id === "bell-states"}
    <div class="bell-states-step">
      <h1>Bell States & EPR Pairs 🔔</h1>
      <p class="lead">
        The mathematical description of maximally entangled two-qubit states.
      </p>

      <Card>
        <h4>The Four Bell States</h4>
        <div class="bell-states-grid">
          <div class="bell-state">
            <div class="state-name">Φ⁺</div>
            <div class="state-formula">(|00⟩ + |11⟩)/√2</div>
            <p class="state-desc">Both qubits always agree</p>
          </div>
          <div class="bell-state">
            <div class="state-name">Φ⁻</div>
            <div class="state-formula">(|00⟩ - |11⟩)/√2</div>
            <p class="state-desc">Both qubits agree (opposite phase)</p>
          </div>
          <div class="bell-state">
            <div class="state-name">Ψ⁺</div>
            <div class="state-formula">(|01⟩ + |10⟩)/√2</div>
            <p class="state-desc">Both qubits always differ</p>
          </div>
          <div class="bell-state">
            <div class="state-name">Ψ⁻</div>
            <div class="state-formula">(|01⟩ - |10⟩)/√2</div>
            <p class="state-desc">Both qubits differ (opposite phase)</p>
          </div>
        </div>
      </Card>

      <Card variant="info">
        <h4>🔬 Creating a Bell State (Φ⁺)</h4>
        <div class="circuit-steps">
          <div class="circuit-step">
            <div class="step-num">1</div>
            <p>Start with two qubits in |00⟩</p>
          </div>
          <div class="arrow-down">↓</div>
          <div class="circuit-step">
            <div class="step-num">2</div>
            <p>Apply Hadamard (H) gate to first qubit</p>
            <p class="small">Creates: (|0⟩ + |1⟩)/√2 ⊗ |0⟩</p>
          </div>
          <div class="arrow-down">↓</div>
          <div class="circuit-step">
            <div class="step-num">3</div>
            <p>Apply CNOT gate (first controls second)</p>
            <p class="small">Result: (|00⟩ + |11⟩)/√2</p>
          </div>
        </div>
      </Card>

      <Card variant="success">
        <h4>💡 What This Means</h4>
        <p>
          The Bell state (|00⟩ + |11⟩)/√2 means: "The two qubits are in a
          superposition where they're either <strong>both 0</strong> or
          <strong>both 1</strong>, with equal probability."
        </p>
        <p>
          You can't describe either qubit independently anymore - they're a
          single entangled system!
        </p>
      </Card>
    </div>
  {:else if $currentStep?.id === "correlation"}
    <div class="correlation-step">
      <h1>Measurement Correlations 📊</h1>
      <p class="lead">
        The magic happens when you measure entangled qubits.
      </p>

      <div class="correlation-demo">
        <div class="measurement-scenario">
          <h4>Scenario: Bell State Φ⁺ = (|00⟩ + |11⟩)/√2</h4>

          <div class="measurement-box">
            <div class="qubit-pair">
              <div class="qubit-visual entangled">
                <span class="qubit-label">Qubit A</span>
                <div class="qubit-state">?</div>
              </div>
              <div class="entangle-link"></div>
              <div class="qubit-visual entangled">
                <span class="qubit-label">Qubit B</span>
                <div class="qubit-state">?</div>
              </div>
            </div>

            <div class="measure-action">
              <p>👉 Measure Qubit A first...</p>
            </div>

            <div class="outcomes">
              <div class="outcome">
                <div class="outcome-header">
                  <span class="probability">50%</span>
                  <span>Outcome 1</span>
                </div>
                <div class="result-pair">
                  <div class="result-box measured">A: 0</div>
                  <span class="arrow-right">→</span>
                  <div class="result-box instant">B: 0</div>
                </div>
                <p class="small">Measure A as 0, B instantly becomes 0!</p>
              </div>

              <div class="outcome">
                <div class="outcome-header">
                  <span class="probability">50%</span>
                  <span>Outcome 2</span>
                </div>
                <div class="result-pair">
                  <div class="result-box measured">A: 1</div>
                  <span class="arrow-right">→</span>
                  <div class="result-box instant">B: 1</div>
                </div>
                <p class="small">Measure A as 1, B instantly becomes 1!</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <Card variant="warning">
        <h4>⚠️ Important!</h4>
        <p>
          <strong>Perfect correlation:</strong> In the Φ⁺ state, A and B
          <strong>always</strong> give the same result (both 0 or both 1).
        </p>
        <p>
          <strong>But which one?</strong> That's random (50/50). You can't
          predict it until you measure.
        </p>
        <p>
          <strong>No communication:</strong> This doesn't allow faster-than-light
          communication because the results are random. You can only see the correlation
          when you compare measurements.
        </p>
      </Card>

      <Card>
        <h4>Different Bell States, Different Correlations</h4>
        <ul class="correlation-list">
          <li><strong>Φ⁺:</strong> Always same (00 or 11)</li>
          <li><strong>Ψ⁺:</strong> Always opposite (01 or 10)</li>
          <li>
            <strong>Φ⁻ and Ψ⁻:</strong> Same correlations but with quantum phase
            differences
          </li>
        </ul>
      </Card>
    </div>
  {:else if $currentStep?.id === "spooky"}
    <div class="spooky-step">
      <h1>Spooky Action at a Distance 👻</h1>
      <p class="lead">
        Why Einstein was troubled by quantum entanglement.
      </p>

      <Card variant="info">
        <div class="einstein-quote">
          <div class="quote-mark">"</div>
          <p class="quote-text">
            Spooky action at a distance... I cannot believe that God plays dice
            with the universe.
          </p>
          <p class="quote-author">— Albert Einstein, 1947</p>
        </div>
      </Card>

      <div class="epr-paradox">
        <h4>🤔 The EPR Paradox (1935)</h4>
        <p>
          Einstein, Podolsky, and Rosen argued that quantum mechanics must be
          incomplete because:
        </p>

        <div class="argument-steps">
          <div class="arg-step">
            <div class="arg-num">1</div>
            <div class="arg-content">
              <p>
                <strong>No faster-than-light signals:</strong> According to relativity,
                nothing can travel faster than light.
              </p>
            </div>
          </div>
          <div class="arg-step">
            <div class="arg-num">2</div>
            <div class="arg-content">
              <p>
                <strong>Instant correlation:</strong> Measuring one entangled particle
                instantly determines the other's state.
              </p>
            </div>
          </div>
          <div class="arg-step">
            <div class="arg-num">3</div>
            <div class="arg-content">
              <p>
                <strong>Their conclusion:</strong> The particles must have had definite
                values all along ("hidden variables"), and quantum mechanics just
                doesn't know them.
              </p>
            </div>
          </div>
        </div>
      </div>

      <Card variant="success">
        <h4>🏆 What Really Happens</h4>
        <p>
          <strong>Bell's Theorem (1964)</strong> and subsequent experiments proved
          Einstein wrong! The universe really does have this "spooky" behavior.
        </p>
        <p>Key insights:</p>
        <ul class="insight-list">
          <li>
            No hidden variables - particles truly don't have definite states
            until measured
          </li>
          <li>
            Entanglement is real, but it doesn't transmit information
            faster-than-light
          </li>
          <li>
            The correlation is instant, but you can't use it to send messages
            (the results are random)
          </li>
          <li>Nature is fundamentally non-local in this quantum way</li>
        </ul>
      </Card>

      <div class="modern-view">
        <h4>🌐 Modern Understanding</h4>
        <p>
          Today we know entanglement is a fundamental feature of quantum
          mechanics, not a bug. It's being used for:
        </p>
        <ul>
          <li>🔐 Quantum cryptography (unbreakable encryption)</li>
          <li>📡 Quantum teleportation (of quantum states)</li>
          <li>💻 Quantum computing (enhanced processing power)</li>
          <li>🌍 Future quantum internet</li>
        </ul>
      </div>
    </div>
  {:else if $currentStep?.id === "demo"}
    <div class="demo-step">
      <h1>Try It Yourself! 🎮</h1>
      <p class="lead">
        Experiment with real entangled quantum states using Qiskit!
      </p>

      <Card variant="info">
        <h4>🔬 What You'll See</h4>
        <p>
          Create Bell states and observe the perfect correlations between
          entangled qubits. Run multiple measurements to see how the results
          always match the expected patterns.
        </p>
        <p class="hint">
          Try all four Bell states and watch how the correlations differ!
        </p>
      </Card>

      <EntanglementDemo />

      <Card variant="success" style="margin-top: 24px;">
        <h4>What Did You Learn?</h4>
        <ul class="learn-list">
          <li>
            <strong>Φ⁺ state:</strong> Qubits always match - both 0 or both 1 with
            50% probability each
          </li>
          <li>
            <strong>Ψ⁺ state:</strong> Qubits always differ - 01 or 10 with 50%
            probability each
          </li>
          <li>
            <strong>Perfect correlation:</strong> No matter the distance, measuring
            one instantly determines the other
          </li>
          <li>
            <strong>Key insight:</strong> This is real quantum randomness with perfect
            correlations - impossible with classical physics!
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