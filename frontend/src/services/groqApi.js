// Groq API service for AI chat assistant
const GROQ_API_URL = 'https://api.groq.com/openai/v1/chat/completions';

// You'll set this in your .env file
const GROQ_API_KEY = import.meta.env.VITE_GROQ_API_KEY || '';

const SYSTEM_PROMPT = `You are a friendly quantum computing tutor helping complete beginners understand quantum concepts. 

Your teaching style:
- Use simple, everyday language (avoid jargon)
- Give real-world analogies that anyone can understand
- Be encouraging and patient
- Keep explanations short (2-3 sentences max)
- Use emojis occasionally to keep it fun 🎯
- If asked about math, explain conceptually first

Current context: The student is learning about quantum superposition through an interactive lesson about quantum coin flips.

Key concepts to help with:
- Superposition: A quantum bit can be in multiple states at once (like a spinning coin)
- Measurement: Observing a quantum state "collapses" it to one definite value
- Hadamard Gate: Creates a 50/50 superposition
- |0⟩ and |1⟩: Quantum states (like heads and tails)

Remember: These are non-technical learners. Make quantum physics feel approachable and fun!`;

export async function sendMessage(messages, currentContext = '') {
    if (!GROQ_API_KEY) {
        throw new Error('Groq API key not configured. Please add VITE_GROQ_API_KEY to your .env file.');
    }

    const contextMessage = currentContext 
        ? `\n\nCurrent lesson step: ${currentContext}`
        : '';

    const apiMessages = [
        {
            role: 'system',
            content: SYSTEM_PROMPT + contextMessage
        },
        ...messages.map(msg => ({
            role: msg.role,
            content: msg.content
        }))
    ];

    try {
        const response = await fetch(GROQ_API_URL, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${GROQ_API_KEY}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                model: 'llama-3.3-70b-versatile',
                messages: apiMessages,
                temperature: 0.7,
                max_tokens: 500,
                top_p: 1,
                stream: false
            })
        });

        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.error?.message || `API error: ${response.status}`);
        }

        const data = await response.json();
        return data.choices[0].message.content;
    } catch (error) {
        if (error.message.includes('API key')) {
            throw error;
        }
        throw new Error(`Failed to get response: ${error.message}`);
    }
}

// Quick question suggestions based on current step
export const questionSuggestions = {
    intro: [
        "What makes quantum different from normal?",
        "Why should I care about quantum computing?",
        "Is this going to be hard to understand?"
    ],
    classical: [
        "Can you give me another example?",
        "Why can't normal computers do this?",
        "What's a bit vs a qubit?"
    ],
    analogy: [
        "How is a spinning coin like superposition?",
        "What happens when I look at the coin?",
        "Is the coin really in two states?"
    ],
    math: [
        "What does |0⟩ mean?",
        "Why is it 50/50 probability?",
        "Can you explain without math?"
    ],
    demo: [
        "Why did I get that result?",
        "Is this truly random?",
        "What's the Hadamard gate doing?"
    ]
};