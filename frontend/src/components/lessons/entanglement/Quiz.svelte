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
      question: "What is quantum entanglement?",
      options: [
        "When two particles are physically connected by a string",
        "When two particles share a quantum state and measuring one affects the other",
        "When particles move at the speed of light",
        "When particles have the same mass"
      ],
      correct: 1,
      explanation: "Entanglement is when two particles share a quantum state. They're correlated in a way that measuring one instantly affects the other, regardless of distance."
    },
    {
      question: "What is a Bell state?",
      options: [
        "A classical correlated state",
        "A state with only one qubit",
        "A maximally entangled two-qubit quantum state",
        "A measurement device"
      ],
      correct: 2,
      explanation: "Bell states are the four maximally entangled two-qubit quantum states, named after physicist John Stewart Bell."
    },
    {
      question: "In the Bell state Φ⁺ = (|00⟩ + |11⟩)/√2, what happens when you measure the first qubit?",
      options: [
        "The second qubit becomes random",
        "The second qubit instantly has the same value as the first",
        "Nothing happens to the second qubit",
        "Both qubits become 0"
      ],
      correct: 1,
      explanation: "In the Φ⁺ state, the qubits are perfectly correlated. If the first is measured as 0, the second instantly becomes 0. If the first is 1, the second is 1."
    },
    {
      question: "How do you create a Bell state (Φ⁺)?",
      options: [
        "Apply two Hadamard gates",
        "Apply a Hadamard gate to the first qubit, then a CNOT gate",
        "Apply only a CNOT gate",
        "Measure both qubits"
      ],
      correct: 1,
      explanation: "To create Φ⁺: Start with |00⟩, apply Hadamard to first qubit (creates superposition), then apply CNOT with first as control (creates entanglement)."
    },
    {
      question: "What did Einstein call entanglement?",
      options: [
        "Quantum magic",
        "Beautiful physics",
        "Spooky action at a distance",
        "Impossible nonsense"
      ],
      correct: 2,
      explanation: "Einstein famously called it 'spooky action at a distance' because he was troubled by how measuring one particle could instantly affect another far away."
    },
    {
      question: "Can quantum entanglement be used to send messages faster than light?",
      options: [
        "Yes, that's its main use",
        "No, because measurement results are random",
        "Yes, but only short messages",
        "Only if the particles are close together"
      ],
      correct: 1,
      explanation: "No! While the correlation is instant, you can't send messages because the measurement results are random. You only see the correlation when you compare results later."
    },
    {
      question: "What was the EPR paradox?",
      options: [
        "A mathematical error in quantum mechanics",
        "An argument that quantum mechanics must be incomplete",
        "Proof that entanglement doesn't exist",
        "A new type of quantum gate"
      ],
      correct: 1,
      explanation: "Einstein, Podolsky, and Rosen argued that quantum mechanics must be incomplete because entanglement seemed to violate locality. Bell's theorem later proved quantum mechanics was right!"
    },
    {
      question: "What's the difference between classical correlation and quantum entanglement?",
      options: [
        "There is no difference",
        "Classical: properties exist before measurement. Quantum: properties are created by measurement",
        "Quantum works only at short distances",
        "Classical is faster"
      ],
      correct: 1,
      explanation: "Key difference: In classical correlation, properties exist beforehand (like shoes in boxes). In entanglement, the particles don't have definite states until measured!"
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
      <p>Let's see what you've learned about entanglement!</p>
      
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
          <p>You've mastered quantum entanglement! You understand Bell states, correlations, and the EPR paradox. Einstein would be impressed!</p>
        {:else if score >= 6}
          <h3>Great Job! 🎉</h3>
          <p>You have a solid understanding of entanglement. You know about spooky action at a distance and Bell states!</p>
        {:else if score >= 4}
          <h3>Good Start! 💪</h3>
          <p>You're getting there! Review the lesson content, especially the sections on Bell states and measurement correlations.</p>
        {:else}
          <h3>Keep Learning! 📚</h3>
          <p>Entanglement is tricky! Take another look at the lesson, try the interactive demo, and retake the quiz.</p>
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