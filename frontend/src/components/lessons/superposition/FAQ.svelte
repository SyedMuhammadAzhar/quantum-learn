<script>
    import './faq.css';
    import { slide } from 'svelte/transition';
    
    let openQuestion = null;
    
    const faqs = [
        {
            id: 1,
            question: "What exactly is superposition?",
            answer: "Imagine a coin spinning in the air - it's neither heads nor tails until it lands. Superposition is similar: a quantum bit (qubit) can be in a mix of both 0 and 1 at the same time, until we measure it!"
        },
        {
            id: 2,
            question: "How is this different from a regular coin flip?",
            answer: "A regular coin is always either heads OR tails - we just don't know which until we look. A quantum coin is actually BOTH at the same time! When we measure it, reality 'chooses' one outcome."
        },
        {
            id: 3,
            question: "Why does measuring collapse the superposition?",
            answer: "Think of it like catching the spinning coin - the act of catching forces it to be either heads or tails. Measuring a qubit forces it to 'pick a side' and become either 0 or 1."
        },
        {
            id: 4,
            question: "Can I see superposition in everyday life?",
            answer: "Not really! Superposition only works at the tiniest scales (atoms and photons). The quantum world has different rules than our everyday world. That's what makes it so special and useful!"
        },
        {
            id: 5,
            question: "Is quantum computing just faster regular computing?",
            answer: "Not exactly! It's fundamentally different. Quantum computers can explore many possibilities at once (thanks to superposition), which makes them amazing for certain problems - but not necessarily all problems."
        },
        {
            id: 6,
            question: "Do I need to know complicated math?",
            answer: "Nope! While quantum physics has complex math, you can understand the concepts without it. We're focusing on the 'what' and 'why', not the heavy equations. 🎯"
        }
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
                <button 
                    class="faq-question" 
                    onclick={() => toggleQuestion(faq.id)}
                >
                    <span class="question-text">{faq.question}</span>
                    <span class="toggle-icon">{openQuestion === faq.id ? '−' : '+'}</span>
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
        <p>💡 <strong>Still curious?</strong> Use the chat assistant to ask more questions!</p>
    </div>
</div>
