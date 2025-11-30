<script>
  import "./faq.css";
  import { slide } from "svelte/transition";

  let openQuestion = null;

  const faqs = [
    {
      id: 1,
      question: "What exactly is superposition?",
      answer:
        "Imagine a coin spinning in the air - it's neither heads nor tails until it lands. Superposition is similar: a quantum bit (qubit) can be in a mix of both 0 and 1 at the same time, until we measure it!",
    },
    {
      id: 2,
      question: "How is this different from a regular coin flip?",
      answer:
        "A regular coin is always either heads OR tails - we just don't know which until we look. A quantum coin is actually BOTH at the same time! When we measure it, reality 'chooses' one outcome.",
    },
    {
      id: 3,
      question: "What is Schrödinger's cat?",
      answer:
        "It's a famous thought experiment! Imagine a cat in a box with a device triggered by a quantum particle. Until you open the box, the cat is theoretically BOTH alive AND dead - in superposition! Of course, this doesn't really happen with cats, but it shows how weird quantum rules would be if they applied to big things. 🐱",
    },
    {
      id: 4,
      question: "Why does measuring collapse the superposition?",
      answer:
        "Think of it like catching the spinning coin - the act of catching forces it to be either heads or tails. Measuring a qubit forces it to 'pick a side' and become either 0 or 1. Scientists are still debating WHY this happens - it's one of the biggest mysteries in physics!",
    },
    {
      id: 5,
      question: "How do scientists actually create superposition?",
      answer:
        "They use special quantum gates, like the Hadamard gate (the 'H' you saw in the demo). It's like a quantum instruction that tells a qubit: 'be both 0 and 1 equally'. Scientists use lasers, microwave pulses, or magnetic fields to apply these gates to real qubits made from atoms, electrons, or photons. ⚛️",
    },
    {
      id: 6,
      question: "What can quantum computers actually do?",
      answer:
        "They're amazing at: 1) Breaking and creating secure codes (cryptography), 2) Simulating molecules for drug discovery, 3) Optimizing complex routes and schedules, 4) Machine learning and AI. But they're NOT faster at everything - your regular computer is still better for browsing the web! 🚀",
    },
    {
      id: 7,
      question: "Can I see superposition in everyday life?",
      answer:
        "Not really! Superposition only works at the tiniest scales (atoms and photons). When quantum systems interact with the environment, they lose superposition - this is called 'decoherence'. That's why quantum computers need to be super cold and isolated!",
    },
    {
      id: 8,
      question: "Is superposition the same as uncertainty?",
      answer:
        "No! Uncertainty means we don't KNOW which state something is in. Superposition means it's genuinely in MULTIPLE states at once. A coin in your closed hand is uncertain (definitely one side, we just don't know). A quantum coin is in superposition (actually both until measured).",
    },
    {
      id: 9,
      question: "Do I need to know complicated math?",
      answer:
        "Nope! While quantum physics has complex math, you can understand the concepts without it. We're focusing on the 'what' and 'why', not the heavy equations. The intuition matters more than the formulas! 🎯",
    },
  ];

  function toggleQuestion(id) {
    openQuestion = openQuestion === id ? null : id;
  }
</script>

<div class="faq-container">
  <div class="faq-header">
    <h2>❓ Frequently Asked Questions</h2>
    <p>Quick answers to common questions about superposition</p>
  </div>

  <div class="faq-list">
    {#each faqs as faq}
      <div class="faq-item" class:open={openQuestion === faq.id}>
        <button class="faq-question" onclick={() => toggleQuestion(faq.id)}>
          <span class="question-text">{faq.question}</span>
          <span class="toggle-icon">{openQuestion === faq.id ? "−" : "+"}</span>
        </button>

        {#if openQuestion === faq.id}
          <div class="faq-answer" transition:slide={{ duration: 300 }}>
            <p>{faq.answer}</p>
          </div>
        {/if}
      </div>
    {/each}
  </div>

  <div class="faq-footer">
    <p>
      💡 <strong>Still curious?</strong> Use the chat assistant to ask more questions!
    </p>
  </div>
</div>
