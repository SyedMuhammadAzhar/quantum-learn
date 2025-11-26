<script>
  import { slide } from 'svelte/transition';
  import './quiz.css';
  import { lessonStore } from "../../../stores/lessonStore.js";

  let currentQuestion = 0;
  let selectedAnswer = null;
  let showFeedback = false;
  let score = 0;
  let quizCompleted = false;
  let answers = [];

  const questions = [
    {
      question: "What happens when you measure a quantum state?",
      options: [
        "Nothing changes, you just learn information",
        "The superposition collapses to a definite state",
        "The qubit becomes entangled",
        "The probability increases"
      ],
      correct: 1,
      explanation: "Measurement causes wavefunction collapse - the quantum state goes from superposition to a definite state (0 or 1). This is irreversible!"
    },
    {
      question: "What is the Born Rule?",
      options: [
        "Quantum states must be normalized",
        "Probability = amplitude",
        "Probability = |amplitude|²",
        "Energy = mass × speed of light²"
      ],
      correct: 2,
      explanation: "The Born Rule states that the probability of measuring a particular outcome is the SQUARE of the amplitude: P = |α|²"
    },
    {
      question: "If a qubit is in state |ψ⟩ = (|0⟩ + |1⟩)/√2, what's the probability of measuring 0?",
      options: [
        "0%",
        "25%",
        "50%",
        "100%"
      ],
      correct: 2,
      explanation: "Using the Born Rule: P(0) = |1/√2|² = 1/2 = 50%. This is an equal superposition state!"
    },
    {
      question: "Can you predict the exact outcome of a single quantum measurement?",
      options: [
        "Yes, if you know the wavefunction",
        "No, it's fundamentally random",
        "Yes, with better equipment",
        "Only for entangled particles"
      ],
      correct: 1,
      explanation: "Quantum mechanics is fundamentally probabilistic. You can only predict probabilities, not individual outcomes. This randomness is a feature, not a limitation!"
    },
    {
      question: "What is a measurement basis?",
      options: [
        "The location where you measure",
        "The direction/way you choose to measure the qubit",
        "The probability distribution",
        "The energy level of the qubit"
      ],
      correct: 1,
      explanation: "A measurement basis is the 'direction' or 'way' you choose to measure. Different bases (Z, X, Y) ask different questions and give different results!"
    },
    {
      question: "In Schrödinger's cat thought experiment, when does the cat become definitely alive or dead?",
      options: [
        "When the radioactive atom decays",
        "When the poison is released",
        "When you open the box and observe",
        "This is still debated!"
      ],
      correct: 3,
      explanation: "This is the measurement problem! When exactly does collapse happen? This question is still actively debated in quantum foundations research."
    },
    {
      question: "If you measure a qubit in state |+⟩ = (|0⟩ + |1⟩)/√2 using the Z-basis, what happens?",
      options: [
        "Always get 0",
        "Always get 1",
        "Get 0 or 1 with 50% probability each",
        "The measurement fails"
      ],
      correct: 2,
      explanation: "The |+⟩ state is an equal superposition in the Z-basis, so measuring in Z-basis gives 50/50 chance of 0 or 1. But if you measured in X-basis, you'd always get |+⟩!"
    },
    {
      question: "Is measurement reversible?",
      options: [
        "Yes, you can undo it",
        "No, it's irreversible",
        "Only for pure states",
        "Only in theory"
      ],
      correct: 1,
      explanation: "Measurement is IRREVERSIBLE. Once you measure and collapse the state, you can't recover the original superposition. Information is lost forever!"
    }
  ];

  function selectAnswer(index) {
    if (showFeedback) return;
    selectedAnswer = index;
  }

  function submitAnswer() {
    if (selectedAnswer === null) return;
    
    showFeedback = true;
    const currentQ = questions[currentQuestion];
    const isCorrect = selectedAnswer === currentQ.correct;
    
    answers[currentQuestion] = {
      questionId: currentQuestion,
      selected: selectedAnswer,
      correct: isCorrect
    };
    
    if (isCorrect) {
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
      if (score >= 6) {
        lessonStore.completeLesson();
      }
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
  $: isCorrect = showFeedback && selectedAnswer === currentQ.correct;
</script>

<div class="quiz-container">
  {#if !quizCompleted}
    <div class="quiz-header">
      <h2>🧠 Test Your Knowledge</h2>
      <p>Let's see what you've learned about quantum measurement!</p>
      
      <div class="progress-bar">
        <div class="progress-fill" style="width: {progress}%"></div>
      </div>
      <p class="progress-text">Question {currentQuestion + 1} of {questions.length}</p>
    </div>

    <div class="question-card">
      <h3 class="question-text">{currentQ.question}</h3>
      
      <div class="options">
        {#each currentQ.options as option, index}
          <button
            class="option"
            class:selected={selectedAnswer === index}
            class:correct={showFeedback && index === currentQ.correct}
            class:incorrect={showFeedback && selectedAnswer === index && !isCorrect}
            class:disabled={showFeedback}
            onclick={() => selectAnswer(index)}
          >
            <span class="option-letter">{String.fromCharCode(65 + index)}</span>
            <span class="option-text">{option}</span>
            {#if showFeedback && index === currentQ.correct}
              <span class="checkmark">✓</span>
            {/if}
            {#if showFeedback && selectedAnswer === index && !isCorrect}
              <span class="crossmark">✗</span>
            {/if}
          </button>
        {/each}
      </div>
      
      {#if showFeedback}
        <div class="feedback" transition:slide={{ duration: 300 }}>
          <div class="feedback-content" class:correct={isCorrect} class:incorrect={!isCorrect}>
            <div class="feedback-icon">
              {isCorrect ? '🎉' : '💡'}
            </div>
            <div class="feedback-text">
              <h4>{isCorrect ? 'Correct!' : 'Not quite!'}</h4>
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
          {score === questions.length ? '🏆' : score >= 6 ? '🌟' : score >= 4 ? '👍' : '📚'}
        </div>
        <h2>Quiz Complete!</h2>
        <p class="score">You scored {score} out of {questions.length}</p>
      </div>
      
      <div class="results-message">
        {#if score >= 7}
          <h3>Outstanding! 🌟</h3>
          <p>You've mastered quantum measurement! You understand collapse, the Born Rule, measurement bases, and even the deep questions like Schrödinger's cat!</p>
        {:else if score >= 6}
          <h3>Great Job! 🎉</h3>
          <p>You have a solid understanding of quantum measurement. You know about wavefunction collapse and the Born Rule!</p>
        {:else if score >= 4}
          <h3>Good Start! 💪</h3>
          <p>You're getting there! Review the lesson content, especially the sections on Born Rule and measurement bases.</p>
        {:else}
          <h3>Keep Learning! 📚</h3>
          <p>Measurement is tricky! Take another look at the lesson, try the interactive demo, and retake the quiz.</p>
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