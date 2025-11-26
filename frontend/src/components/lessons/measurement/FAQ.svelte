<script>
  import './faq.css';
  import Card from "../../ui/Card.svelte";

  const faqs = [
    {
      question: "Does observation really change quantum reality?",
      answer: "Yes! This is one of the most mind-bending aspects of quantum mechanics. Before measurement, a quantum system exists in superposition - multiple states at once. The act of measurement forces it to 'choose' one definite state. This isn't just about disturbing the system - it's a fundamental feature of quantum mechanics where observation literally creates reality from possibilities."
    },
    {
      question: "Can you measure without disturbing the quantum state?",
      answer: "No, measurement always disturbs the quantum state through wavefunction collapse. This is different from classical measurement where you can measure without significantly affecting what you're measuring. In quantum mechanics, measurement is an irreversible interaction that fundamentally changes the system from superposition to a definite state."
    },
    {
      question: "What exactly is the 'measurement problem'?",
      answer: "The measurement problem is the question: When exactly does wavefunction collapse happen? Is it when particles interact? When a conscious observer looks? This is still debated! Different interpretations of quantum mechanics (Copenhagen, Many-Worlds, de Broglie-Bohm) give different answers. It's one of the deepest unsolved questions in physics."
    },
    {
      question: "Why are measurement results random but probabilities predictable?",
      answer: "Quantum mechanics is fundamentally probabilistic. While you can't predict individual measurement outcomes (they're truly random), the probabilities are precisely determined by the wavefunction through the Born Rule. Run many measurements and you'll see the predicted probability distribution emerge. This randomness is not due to hidden variables - experiments have proven it's fundamental."
    },
    {
      question: "What's the difference between measuring in different bases?",
      answer: "Different bases are like asking different questions to the same quantum state. Z-basis asks 'is it 0 or 1?', X-basis asks 'is it + or -?'. A state that's definite in one basis can be a superposition in another. For example, |+⟩ is definite in X-basis but 50/50 superposition in Z-basis. The basis you choose dramatically affects your measurement results!"
    },
    {
      question: "Is Schrödinger's cat actually both alive and dead?",
      answer: "Schrödinger's cat was meant to show how absurd superposition seems at macroscopic scales. In practice, large objects like cats interact so strongly with their environment (decoherence) that superposition can't be maintained. The cat would effectively 'measure' itself almost instantly. True quantum superposition only persists for well-isolated microscopic systems like individual atoms or photons."
    },
    {
      question: "Can you reverse a measurement?",
      answer: "No, measurement is irreversible. Once you collapse a superposition by measuring, you cannot recover the original quantum state. Information is genuinely lost in the measurement process. This is unlike classical measurements where, in principle, everything is reversible. The irreversibility of quantum measurement is connected to the second law of thermodynamics and entropy."
    },
    {
      question: "How do quantum computers measure qubits?",
      answer: "Quantum computers measure qubits at the end of a computation to read out results. The measurement collapses the quantum state to classical bits (0s and 1s). During computation, qubits stay in superposition and entanglement. Many quantum algorithms run the same circuit multiple times to build up statistics, because each measurement gives only one random outcome from the probability distribution."
    }
  ];

  let openIndex = null;

  function toggle(index) {
    openIndex = openIndex === index ? null : index;
  }
</script>

<div class="faq-container">
  <h1>Frequently Asked Questions 💭</h1>
  <p class="lead">
    Common questions about quantum measurement, answered!
  </p>

  <div class="faq-list">
    {#each faqs as faq, index}
      <div class="faq-item" class:open={openIndex === index}>
        <button class="faq-question" on:click={() => toggle(index)}>
          <span class="question-text">{faq.question}</span>
          <span class="toggle-icon">{openIndex === index ? "−" : "+"}</span>
        </button>
        {#if openIndex === index}
          <div class="faq-answer">
            <Card>
              <p>{faq.answer}</p>
            </Card>
          </div>
        {/if}
      </div>
    {/each}
  </div>

  <Card variant="info" style="margin-top: 32px;">
    <h4>🤔 Still Have Questions?</h4>
    <p>
      Quantum measurement is genuinely strange - even physicists debate its interpretation!
      If you're confused, you're in good company.
    </p>
    <p>
      The key is to accept that quantum mechanics sometimes defies classical
      intuition. Measurement fundamentally changes reality at the quantum level!
    </p>
  </Card>
</div>