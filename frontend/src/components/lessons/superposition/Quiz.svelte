<script>
    import { slide } from 'svelte/transition';
    import Card from '../../ui/Card.svelte';
    
    let currentQuestion = 0;
    let selectedAnswer = null;
    let showFeedback = false;
    let score = 0;
    let quizCompleted = false;
    let answers = [];
    
    const questions = [
        {
            id: 1,
            question: "What is the main difference between a classical bit and a quantum bit (qubit)?",
            options: [
                { id: 'a', text: 'A bit is faster than a qubit', correct: false },
                { id: 'b', text: 'A qubit can be 0 and 1 at the same time (superposition)', correct: true },
                { id: 'c', text: 'A bit stores more information than a qubit', correct: false },
                { id: 'd', text: 'There is no difference', correct: false }
            ],
            explanation: "Correct! A classical bit is always either 0 OR 1, but a qubit can be in superposition - both 0 AND 1 simultaneously until measured. This is what makes quantum computing special! 🎯"
        },
        {
            id: 2,
            question: "What happens when you measure a qubit in superposition?",
            options: [
                { id: 'a', text: 'Nothing happens, it stays the same', correct: false },
                { id: 'b', text: 'It becomes both 0 and 1', correct: false },
                { id: 'c', text: 'The superposition collapses to either 0 or 1', correct: true },
                { id: 'd', text: 'It disappears', correct: false }
            ],
            explanation: "Exactly! Measurement forces the qubit to 'choose' - it collapses from superposition to a definite value (0 or 1). Like catching a spinning coin makes it land on one side! 🪙"
        },
        {
            id: 3,
            question: "In the spinning coin analogy, what does the spinning represent?",
            options: [
                { id: 'a', text: 'The qubit being broken', correct: false },
                { id: 'b', text: 'The qubit being in superposition', correct: true },
                { id: 'c', text: 'The qubit being measured', correct: false },
                { id: 'd', text: 'A classical bit', correct: false }
            ],
            explanation: "Perfect! The spinning coin represents superposition - the qubit is in a mix of both states at once, just like the coin shows both heads and tails while spinning. ✨"
        },
        {
            id: 4,
            question: "Why can't we see superposition in everyday objects?",
            options: [
                { id: 'a', text: 'We can, we just don\'t notice it', correct: false },
                { id: 'b', text: 'Superposition only works at tiny scales (atoms, photons)', correct: true },
                { id: 'c', text: 'Superposition doesn\'t exist', correct: false },
                { id: 'd', text: 'Our eyes are too slow', correct: false }
            ],
            explanation: "Right! Superposition is a quantum effect that only works at incredibly tiny scales. The bigger an object, the harder it is to keep in superposition. That's why we don't see everyday objects in two places at once! 🔬"
        },
        {
            id: 5,
            question: "What makes quantum computers potentially more powerful than classical computers?",
            options: [
                { id: 'a', text: 'They use less electricity', correct: false },
                { id: 'b', text: 'They can explore many possibilities at once using superposition', correct: true },
                { id: 'c', text: 'They are just faster versions of regular computers', correct: false },
                { id: 'd', text: 'They never make mistakes', correct: false }
            ],
            explanation: "Spot on! Thanks to superposition, quantum computers can explore many solutions simultaneously instead of checking them one by one. This makes them incredibly powerful for certain types of problems! 🚀"
        }
    ];
    
    function selectAnswer(optionId) {
        if (showFeedback) return; // Prevent changing answer after submission
        selectedAnswer = optionId;
    }
    
    function submitAnswer() {
        if (selectedAnswer === null) return;
        
        showFeedback = true;
        const currentQ = questions[currentQuestion];
        const selectedOption = currentQ.options.find(opt => opt.id === selectedAnswer);
        
        answers[currentQuestion] = {
            questionId: currentQ.id,
            selected: selectedAnswer,
            correct: selectedOption.correct
        };
        
        if (selectedOption.correct) {
            score++;
        }
    }
    
    function nextQuestion() {
        if (currentQuestion < questions.length - 1) {
            currentQuestion++;
            selectedAnswer = null;
            showFeedback = false;
        } else {
            quizCompleted = true;
        }
    }
    
    function restartQuiz() {
        currentQuestion = 0;
        selectedAnswer = null;
        showFeedback = false;
        score = 0;
        quizCompleted = false;
        answers = [];
    }
    
    $: progress = ((currentQuestion + 1) / questions.length) * 100;
    $: currentQ = questions[currentQuestion];
    $: selectedOption = currentQ?.options.find(opt => opt.id === selectedAnswer);
</script>

<div class="quiz-container">
    {#if !quizCompleted}
        <div class="quiz-header">
            <h2>🧠 Test Your Knowledge</h2>
            <p>Let's see what you've learned about superposition!</p>
            
            <div class="progress-bar">
                <div class="progress-fill" style="width: {progress}%"></div>
            </div>
            <p class="progress-text">Question {currentQuestion + 1} of {questions.length}</p>
        </div>
        
        <div class="question-card">
            <h3 class="question-text">{currentQ.question}</h3>
            
            <div class="options">
                {#each currentQ.options as option}
                    <button
                        class="option"
                        class:selected={selectedAnswer === option.id}
                        class:correct={showFeedback && option.correct}
                        class:incorrect={showFeedback && selectedAnswer === option.id && !option.correct}
                        class:disabled={showFeedback}
                        onclick={() => selectAnswer(option.id)}
                    >
                        <span class="option-letter">{option.id.toUpperCase()}</span>
                        <span class="option-text">{option.text}</span>
                        {#if showFeedback && option.correct}
                            <span class="checkmark">✓</span>
                        {/if}
                        {#if showFeedback && selectedAnswer === option.id && !option.correct}
                            <span class="crossmark">✗</span>
                        {/if}
                    </button>
                {/each}
            </div>
            
            {#if showFeedback}
                <div class="feedback" transition:slide={{ duration: 300 }}>
                    <div class="feedback-content" class:correct={selectedOption?.correct} class:incorrect={!selectedOption?.correct}>
                        <div class="feedback-icon">
                            {selectedOption?.correct ? '🎉' : '💡'}
                        </div>
                        <div class="feedback-text">
                            <h4>{selectedOption?.correct ? 'Correct!' : 'Not quite!'}</h4>
                            <p>{currentQ.explanation}</p>
                        </div>
                    </div>
                </div>
            {/if}
            
            <div class="button-group">
                {#if !showFeedback}
                    <button 
                        class="btn btn-primary" 
                        onclick={submitAnswer}
                        disabled={selectedAnswer === null}
                    >
                        Submit Answer
                    </button>
                {:else}
                    <button class="btn btn-primary" onclick={nextQuestion}>
                        {currentQuestion < questions.length - 1 ? 'Next Question →' : 'See Results 🎯'}
                    </button>
                {/if}
            </div>
        </div>
    {:else}
        <div class="results">
            <div class="results-header">
                <div class="results-emoji">
                    {score === questions.length ? '🏆' : score >= 4 ? '🌟' : score >= 3 ? '👍' : '📚'}
                </div>
                <h2>Quiz Complete!</h2>
                <p class="score">You scored {score} out of {questions.length}</p>
            </div>
            
            <div class="results-message">
                {#if score === questions.length}
                    <h3>Perfect Score! 🎉</h3>
                    <p>You've mastered the basics of superposition! You're ready to explore more quantum concepts.</p>
                {:else if score >= 4}
                    <h3>Great Job! 🌟</h3>
                    <p>You have a solid understanding of superposition. Keep learning!</p>
                {:else if score >= 3}
                    <h3>Good Effort! 👍</h3>
                    <p>You're getting there! Review the lesson and try again to improve your score.</p>
                {:else}
                    <h3>Keep Learning! 📚</h3>
                    <p>Don't worry! Quantum physics is tricky. Review the lesson and give it another shot.</p>
                {/if}
            </div>
            
            <div class="button-group">
                <button class="btn btn-secondary" onclick={restartQuiz}>
                    🔄 Retake Quiz
                </button>
            </div>
        </div>
    {/if}
</div>

<style>
    .quiz-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 2rem;
    }
    
    .quiz-header {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .quiz-header h2 {
        font-size: 2rem;
        margin-bottom: 0.5rem;
        color: #2d3748;
    }
    
    .quiz-header p {
        color: #718096;
        font-size: 1rem;
        margin-bottom: 1.5rem;
    }
    
    .progress-bar {
        width: 100%;
        height: 8px;
        background: #e2e8f0;
        border-radius: 999px;
        overflow: hidden;
        margin-bottom: 0.5rem;
    }
    
    .progress-fill {
        height: 100%;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        transition: width 0.3s ease;
    }
    
    .progress-text {
        font-size: 0.875rem;
        color: #718096;
        font-weight: 600;
    }
    
    .question-card {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    }
    
    .question-text {
        font-size: 1.375rem;
        font-weight: 600;
        color: #2d3748;
        margin-bottom: 2rem;
        line-height: 1.5;
    }
    
    .options {
        display: flex;
        flex-direction: column;
        gap: 1rem;
        margin-bottom: 2rem;
    }
    
    .option {
        display: flex;
        align-items: center;
        gap: 1rem;
        padding: 1.25rem 1.5rem;
        background: #f7fafc;
        border: 2px solid #e2e8f0;
        border-radius: 12px;
        cursor: pointer;
        transition: all 0.2s ease;
        text-align: left;
        position: relative;
    }
    
    .option:hover:not(.disabled) {
        border-color: #667eea;
        background: #f0f4ff;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.1);
    }
    
    .option.selected:not(.correct):not(.incorrect) {
        border-color: #667eea;
        background: #e9ecff;
    }
    
    .option.correct {
        border-color: #48bb78;
        background: #f0fff4;
    }
    
    .option.incorrect {
        border-color: #f56565;
        background: #fff5f5;
    }
    
    .option.disabled {
        cursor: not-allowed;
    }
    
    .option-letter {
        width: 36px;
        height: 36px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: #667eea;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        flex-shrink: 0;
    }
    
    .option.correct .option-letter {
        background: #48bb78;
    }
    
    .option.incorrect .option-letter {
        background: #f56565;
    }
    
    .option-text {
        flex: 1;
        font-size: 1rem;
        color: #2d3748;
        font-weight: 500;
    }
    
    .checkmark, .crossmark {
        font-size: 1.5rem;
        font-weight: bold;
        flex-shrink: 0;
    }
    
    .checkmark {
        color: #48bb78;
    }
    
    .crossmark {
        color: #f56565;
    }
    
    .feedback {
        margin-top: 1.5rem;
    }
    
    .feedback-content {
        display: flex;
        gap: 1rem;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid;
    }
    
    .feedback-content.correct {
        background: #f0fff4;
        border-color: #48bb78;
    }
    
    .feedback-content.incorrect {
        background: #fffaf0;
        border-color: #ed8936;
    }
    
    .feedback-icon {
        font-size: 2rem;
        flex-shrink: 0;
    }
    
    .feedback-text h4 {
        margin: 0 0 0.5rem 0;
        font-size: 1.125rem;
        color: #2d3748;
    }
    
    .feedback-text p {
        margin: 0;
        color: #4a5568;
        line-height: 1.6;
    }
    
    .button-group {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin-top: 2rem;
    }
    
    .btn {
        padding: 0.875rem 2rem;
        border: none;
        border-radius: 10px;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s ease;
    }
    
    .btn-primary {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    .btn-primary:hover:not(:disabled) {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    .btn-primary:disabled {
        opacity: 0.5;
        cursor: not-allowed;
    }
    
    .btn-secondary {
        background: white;
        color: #667eea;
        border: 2px solid #667eea;
    }
    
    .btn-secondary:hover {
        background: #667eea;
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.3);
    }
    
    .results {
        text-align: center;
        background: white;
        border-radius: 16px;
        padding: 3rem 2rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    }
    
    .results-header {
        margin-bottom: 2rem;
    }
    
    .results-emoji {
        font-size: 5rem;
        margin-bottom: 1rem;
    }
    
    .results h2 {
        font-size: 2rem;
        color: #2d3748;
        margin-bottom: 1rem;
    }
    
    .score {
        font-size: 1.5rem;
        font-weight: 700;
        color: #667eea;
    }
    
    .results-message {
        background: #f7fafc;
        border-radius: 12px;
        padding: 2rem;
        margin-bottom: 2rem;
    }
    
    .results-message h3 {
        font-size: 1.5rem;
        color: #2d3748;
        margin-bottom: 0.5rem;
    }
    
    .results-message p {
        color: #4a5568;
        font-size: 1.125rem;
        line-height: 1.6;
    }
    
    @media (max-width: 640px) {
        .quiz-container {
            padding: 1rem;
        }
        
        .question-card {
            padding: 1.5rem;
        }
        
        .question-text {
            font-size: 1.125rem;
        }
        
        .option {
            padding: 1rem;
        }
        
        .option-text {
            font-size: 0.9375rem;
        }
        
        .results {
            padding: 2rem 1.5rem;
        }
    }
</style>
