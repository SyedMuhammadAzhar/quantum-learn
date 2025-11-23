<script>
  import './faq.css';
  import Card from "../../ui/Card.svelte";

  const faqs = [
    {
      question: "How can entanglement happen instantly? Doesn't that violate relativity?",
      answer: "Good question! The connection between particles is instant, but you can't actually send messages with it. Each measurement gives a random result (0 or 1), so there's no way to control what information gets 'sent'. You only see the pattern when you compare results later. Since no real information travels faster than light, Einstein's rules are safe!"
    },
    {
      question: "Does entanglement mean particles are 'talking' to each other?",
      answer: "Not exactly! It's better to think of them as sharing a single state, like two sides of the same coin. They're one connected system, not two separate things sending signals. When you measure one particle, you learn about their shared state, which instantly tells you what the other one will be."
    },
    {
      question: "Can I entangle more than two particles?",
      answer: "Yes! You can entangle 3, 4, or even hundreds of particles together. Scientists call these 'multi-particle entangled states'. They're super useful for building quantum computers and secure communication networks. The more particles you entangle, the more powerful the quantum effects!"
    },
    {
      question: "How long does entanglement last?",
      answer: "In theory, forever! But in real life, things in the environment (like air molecules, light, or heat) can bump into your particles and break the entanglement. This is called 'decoherence'. Scientists use special equipment to protect entangled particles. They've kept some entangled for days, and sent entangled light particles hundreds of kilometers!"
    },
    {
      question: "What's the difference between all four Bell states?",
      answer: "All four Bell states are maximally entangled, but they have different patterns. Φ⁺ makes both particles always match (both 0 or both 1). Ψ⁺ makes them always opposite (one is 0, the other is 1). Φ⁻ and Ψ⁻ are similar but have a 'phase difference' which affects how they interact with other quantum operations."
    },
    {
      question: "What proved Einstein wrong about entanglement?",
      answer: "In 1964, physicist John Bell created a test that could prove whether particles had hidden predetermined values (Einstein's idea) or if quantum mechanics was truly random. Starting in 1982, experiments by Alain Aspect and others showed quantum mechanics was right! Particles really don't have set values until you measure them. Aspect won the Nobel Prize in 2022 for this!"
    },
    {
      question: "What's quantum teleportation?",
      answer: "It's a way to transfer quantum information from one place to another using entanglement. You're not moving actual matter (sorry, no Star Trek!), just the quantum state. Here's how: 1) Share an entangled pair between two places, 2) Do a special measurement, 3) Send a regular message to complete the transfer. It still can't go faster than light!"
    },
    {
      question: "How is entanglement used in quantum computing?",
      answer: "Entanglement is what makes quantum computers so powerful! It lets qubits work together in ways that regular computer bits can't. When qubits are entangled, they can explore many possibilities at the same time. This is why quantum computers can solve certain problems way faster than regular computers!"
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
    Common questions about quantum entanglement, answered!
  </p>

  <div class="faq-list">
    {#each faqs as faq, index}
      <div class="faq-item" class:open={openIndex === index}>
        <button class="faq-question" onclick={() => toggle(index)}>
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
      Entanglement is one of the deepest concepts in quantum mechanics. If
      you're confused, you're in good company - even Einstein struggled with it!
    </p>
    <p>
      The key is to accept that quantum mechanics sometimes defies our classical
      intuition. That's what makes it so fascinating!
    </p>
  </Card>
</div>