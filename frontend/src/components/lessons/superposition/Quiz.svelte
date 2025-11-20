<script>
    import { slide } from 'svelte/transition';
    import quizData from '../../../data/quiz/superposition.json';
    import './quiz.css';
    
    let currentQuestion = 0;
    let selectedAnswer = null;
    let showFeedback = false;
    let score = 0;
    let quizCompleted = false;
    let answers = [];
    
    const questions = quizData.questions;
    
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
    
    function previousQuestion() {
        if (currentQuestion > 0) {
            currentQuestion--;
            selectedAnswer = answers[currentQuestion - 1]?.selected || null;
            showFeedback = false;
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
                {#if currentQuestion > 0 && !showFeedback}
                    <button class="btn btn-secondary" onclick={previousQuestion}>
                        ← Back
                    </button>
                {/if}
                
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
