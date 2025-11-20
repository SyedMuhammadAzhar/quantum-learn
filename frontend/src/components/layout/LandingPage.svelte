<script>
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

<style>
  .landing-page {
    max-width: 1200px;
    margin: 0 auto;
  }

  .hero {
    text-align: center;
    margin-bottom: var(--spacing-2xl);
  }

  .hero-title {
    font-size: 64px;
    margin: 0 0 var(--spacing-md) 0;
    color: white;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
  }

  .hero-subtitle {
    font-size: var(--font-size-xl);
    color: rgba(255, 255, 255, 0.9);
    line-height: 1.6;
    margin: 0;
  }

  .lessons-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: var(--spacing-lg);
    margin-bottom: var(--spacing-2xl);
  }

  .lesson-card {
    background: var(--color-surface);
    border-radius: var(--radius-xl);
    padding: var(--spacing-xl);
    text-align: center;
    cursor: pointer;
    transition:
      transform var(--transition-normal),
      box-shadow var(--transition-normal);
    border: 3px solid transparent;
    position: relative;
    overflow: hidden;
  }

  .lesson-card::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 6px;
    background: var(--card-color);
  }

  .lesson-card:hover:not(:disabled) {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
    border-color: var(--card-color);
  }

  .lesson-card:disabled {
    opacity: 0.7;
    cursor: not-allowed;
  }

  .lesson-card.locked {
    background: #f5f5f5;
  }

  .card-icon {
    font-size: 64px;
    margin-bottom: var(--spacing-md);
  }

  .card-title {
    font-size: var(--font-size-2xl);
    color: var(--color-text-primary);
    margin: 0 0 var(--spacing-sm) 0;
  }

  .card-subtitle {
    color: var(--color-text-muted);
    margin: 0 0 var(--spacing-lg) 0;
    font-size: var(--font-size-base);
  }

  .locked-badge {
    background: var(--color-border);
    color: var(--color-text-muted);
    padding: var(--spacing-sm) var(--spacing-md);
    border-radius: var(--radius-full);
    font-size: var(--font-size-sm);
    font-weight: 600;
    display: inline-block;
  }

  .start-badge {
    background: var(--card-color);
    color: white;
    padding: var(--spacing-sm) var(--spacing-lg);
    border-radius: var(--radius-full);
    font-size: var(--font-size-base);
    font-weight: 600;
    display: inline-block;
    transition: transform var(--transition-fast);
  }

  .lesson-card:hover .start-badge {
    transform: scale(1.05);
  }

  .step-count {
    position: absolute;
    top: var(--spacing-md);
    right: var(--spacing-md);
    background: rgba(0, 0, 0, 0.1);
    padding: var(--spacing-xs) var(--spacing-sm);
    border-radius: var(--radius-md);
    font-size: var(--font-size-xs);
    color: var(--color-text-muted);
  }

  .features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: var(--spacing-lg);
    background: rgba(255, 255, 255, 0.1);
    padding: var(--spacing-xl);
    border-radius: var(--radius-xl);
  }

  .feature {
    text-align: center;
    color: white;
  }

  .feature-icon {
    font-size: 48px;
    display: block;
    margin-bottom: var(--spacing-sm);
  }

  .feature h4 {
    margin: 0 0 var(--spacing-xs) 0;
    font-size: var(--font-size-lg);
  }

  .feature p {
    margin: 0;
    opacity: 0.8;
    font-size: var(--font-size-sm);
  }
</style>
