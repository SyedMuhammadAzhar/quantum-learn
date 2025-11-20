<script>
  import './landingPage.css';
  import { lessons, lessonStore } from "../../stores/lessonStore.js";

  function startLesson(lessonId) {
    const lesson = lessons[lessonId];
    if (lesson && !lesson.locked) {
      lessonStore.startLesson(lessonId);
    }
  }
</script>

<div class="landing-page">
  <div class="hero">
    <h1 class="hero-title">🔬 QuantumLearn</h1>
    <p class="hero-subtitle">
      Master quantum computing through interactive lessons and hands-on
      experiments.
      <br />No physics degree required!
    </p>
  </div>

  <div class="lessons-grid">
    {#each Object.values(lessons) as lesson}
      <button
        class="lesson-card"
        class:locked={lesson.locked}
        style="--card-color: {lesson.color}"
        onclick={() => startLesson(lesson.id)}
        disabled={lesson.locked}
      >
        <div class="card-icon">{lesson.icon}</div>
        <h3 class="card-title">{lesson.title}</h3>
        <p class="card-subtitle">{lesson.subtitle}</p>

        {#if lesson.locked}
          <div class="locked-badge">🔒 Coming Soon</div>
        {:else}
          <div class="start-badge">Start Learning →</div>
        {/if}

        {#if lesson.steps.length > 0}
          <div class="step-count">{lesson.steps.length} steps</div>
        {/if}
      </button>
    {/each}
  </div>

  <div class="features">
    <div class="feature">
      <span class="feature-icon">📚</span>
      <h4>Interactive Lessons</h4>
      <p>Learn at your own pace with visual explanations</p>
    </div>
    <div class="feature">
      <span class="feature-icon">🎮</span>
      <h4>Hands-on Demos</h4>
      <p>Experiment with real quantum simulations</p>
    </div>
    <div class="feature">
      <span class="feature-icon">🤖</span>
      <h4>AI Tutor</h4>
      <p>Ask questions anytime, get instant help</p>
    </div>
  </div>
</div>
