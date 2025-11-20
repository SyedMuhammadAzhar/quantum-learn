<script>
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

<style>
    .faq-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 2rem;
    }
    
    .faq-header {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .faq-header h2 {
        font-size: 2rem;
        margin-bottom: 0.5rem;
        color: #2d3748;
    }
    
    .faq-header p {
        color: #718096;
        font-size: 1rem;
    }
    
    .faq-list {
        display: flex;
        flex-direction: column;
        gap: 1rem;
    }
    
    .faq-item {
        background: white;
        border: 2px solid #e2e8f0;
        border-radius: 12px;
        overflow: hidden;
        transition: all 0.3s ease;
    }
    
    .faq-item:hover {
        border-color: #667eea;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.1);
    }
    
    .faq-item.open {
        border-color: #667eea;
        box-shadow: 0 4px 16px rgba(102, 126, 234, 0.15);
    }
    
    .faq-question {
        width: 100%;
        padding: 1.25rem 1.5rem;
        background: none;
        border: none;
        display: flex;
        justify-content: space-between;
        align-items: center;
        cursor: pointer;
        text-align: left;
        transition: background 0.2s ease;
    }
    
    .faq-question:hover {
        background: #f7fafc;
    }
    
    .question-text {
        font-size: 1.1rem;
        font-weight: 600;
        color: #2d3748;
        flex: 1;
        padding-right: 1rem;
    }
    
    .toggle-icon {
        width: 32px;
        height: 32px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: #667eea;
        color: white;
        border-radius: 50%;
        font-size: 1.5rem;
        font-weight: bold;
        flex-shrink: 0;
        transition: transform 0.3s ease;
    }
    
    .faq-item.open .toggle-icon {
        transform: rotate(180deg);
    }
    
    .faq-answer {
        padding: 0 1.5rem 1.5rem 1.5rem;
        background: #f7fafc;
    }
    
    .faq-answer p {
        margin: 0;
        color: #4a5568;
        font-size: 1rem;
        line-height: 1.6;
    }
    
    .faq-footer {
        margin-top: 2rem;
        padding: 1.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 12px;
        text-align: center;
    }
    
    .faq-footer p {
        margin: 0;
        color: white;
        font-size: 1rem;
    }
    
    @media (max-width: 640px) {
        .faq-container {
            padding: 1rem;
        }
        
        .faq-header h2 {
            font-size: 1.5rem;
        }
        
        .question-text {
            font-size: 1rem;
        }
        
        .faq-question {
            padding: 1rem;
        }
    }
</style>
