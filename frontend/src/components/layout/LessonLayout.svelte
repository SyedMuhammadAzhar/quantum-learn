<script>
  import {
    lessonStore,
    currentLesson,
    currentStep,
    lessonProgress,
  } from "../../stores/lessonStore.js";
  import Button from "../ui/Button.svelte";

  let { children } = $props();

  function handleExit() {
    lessonStore.exitLesson();
  }

  function handleNext() {
    if ($lessonStore.currentStepIndex === $currentLesson.steps.length - 1) {
      lessonStore.completeLesson();
      lessonStore.exitLesson();
    } else {
      lessonStore.nextStep();
    }
  }

  function handlePrevious() {
    lessonStore.previousStep();
  }

  function goToStep(index) {
    lessonStore.goToStep(index);
  }

  let isLastStep = $derived(
    $lessonStore.currentStepIndex === $currentLesson?.steps.length - 1
  );
  let isFirstStep = $derived($lessonStore.currentStepIndex === 0);
</script>

{#if $currentLesson}
  <div class="lesson-layout">
    <!-- Sidebar -->
    <aside class="sidebar">
      <div class="sidebar-header">
        <button class="exit-btn" onclick={handleExit}> ← Back to Home </button>
        <div class="lesson-info">
          <span class="lesson-icon">{$currentLesson.icon}</span>
          <h2 class="lesson-title">{$currentLesson.title}</h2>
        </div>
      </div>

      <div class="progress-section">
        <div class="progress-label">Progress</div>
        <div class="progress-bar">
          <div class="progress-fill" style="width: {$lessonProgress}%"></div>
        </div>
        <div class="progress-text">{$lessonProgress}% Complete</div>
      </div>

      <nav class="step-nav">
        {#each $currentLesson.steps as step, index}
          <button
            class="step-item"
            class:active={index === $lessonStore.currentStepIndex}
            class:completed={$lessonStore.completedSteps[
              $currentLesson.id
            ]?.includes(step.id)}
            onclick={() => goToStep(index)}
          >
            <span class="step-number">{index + 1}</span>
            <span class="step-title">{step.title}</span>
            {#if $lessonStore.completedSteps[$currentLesson.id]?.includes(step.id)}
              <span class="step-check">✓</span>
            {/if}
          </button>
        {/each}
      </nav>
    </aside>

    <!-- Main Content -->
    <main class="lesson-main">
      <div class="lesson-content">
        {@render children()}
      </div>

      <!-- Navigation -->
      <div class="lesson-navigation">
        <Button
          variant="secondary"
          onclick={handlePrevious}
          disabled={isFirstStep}
        >
          ← Previous
        </Button>

        <div class="step-indicator">
          Step {$lessonStore.currentStepIndex + 1} of {$currentLesson.steps
            .length}
        </div>

        <Button
          variant={isLastStep ? "success" : "primary"}
          onclick={handleNext}
        >
          {isLastStep ? "Complete Lesson ✓" : "Next →"}
        </Button>
      </div>
    </main>
  </div>
{/if}

<style>
  .lesson-layout {
    display: grid;
    grid-template-columns: 280px 1fr;
    min-height: 100vh;
    background: var(--color-background);
  }

  .sidebar {
    background: var(--color-surface);
    border-right: 1px solid var(--color-border);
    padding: var(--spacing-lg);
    display: flex;
    flex-direction: column;
    gap: var(--spacing-lg);
  }

  .sidebar-header {
    display: flex;
    flex-direction: column;
    gap: var(--spacing-md);
  }

  .exit-btn {
    background: none;
    border: none;
    color: var(--color-text-muted);
    cursor: pointer;
    padding: var(--spacing-sm);
    text-align: left;
    font-size: var(--font-size-sm);
    transition: color var(--transition-fast);
  }

  .exit-btn:hover {
    color: var(--color-primary);
  }

  .lesson-info {
    display: flex;
    align-items: center;
    gap: var(--spacing-sm);
  }

  .lesson-icon {
    font-size: 32px;
  }

  .lesson-title {
    margin: 0;
    font-size: var(--font-size-xl);
    color: var(--color-text-primary);
  }

  .progress-section {
    background: var(--color-background);
    padding: var(--spacing-md);
    border-radius: var(--radius-md);
  }

  .progress-label {
    font-size: var(--font-size-sm);
    font-weight: 600;
    color: var(--color-text-muted);
    margin-bottom: var(--spacing-sm);
  }

  .progress-bar {
    height: 8px;
    background: var(--color-border);
    border-radius: var(--radius-full);
    overflow: hidden;
    margin-bottom: var(--spacing-xs);
  }

  .progress-fill {
    height: 100%;
    background: var(--color-primary);
    border-radius: var(--radius-full);
    transition: width 0.5s ease;
  }

  .progress-text {
    font-size: var(--font-size-xs);
    color: var(--color-text-muted);
    text-align: right;
  }

  .step-nav {
    display: flex;
    flex-direction: column;
    gap: var(--spacing-xs);
  }

  .step-item {
    display: flex;
    align-items: center;
    gap: var(--spacing-sm);
    padding: var(--spacing-sm) var(--spacing-md);
    background: none;
    border: none;
    border-radius: var(--radius-md);
    cursor: pointer;
    transition: background var(--transition-fast);
    text-align: left;
  }

  .step-item:hover {
    background: var(--color-background);
  }

  .step-item.active {
    background: var(--color-primary);
    color: white;
  }

  .step-item.completed .step-number {
    background: var(--color-success);
    color: white;
  }

  .step-number {
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background: var(--color-border);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: var(--font-size-xs);
    font-weight: 600;
    flex-shrink: 0;
  }

  .step-item.active .step-number {
    background: rgba(255, 255, 255, 0.3);
  }

  .step-title {
    font-size: var(--font-size-sm);
    flex: 1;
  }

  .step-check {
    color: var(--color-success);
    font-weight: bold;
  }

  .step-item.active .step-check {
    color: white;
  }

  .lesson-main {
    display: flex;
    flex-direction: column;
    padding: var(--spacing-xl);
    overflow-y: auto;
  }

  .lesson-content {
    flex: 1;
    max-width: 900px;
    margin: 0 auto;
    width: 100%;
  }

  .lesson-navigation {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: var(--spacing-xl);
    padding-top: var(--spacing-lg);
    border-top: 1px solid var(--color-border);
    max-width: 900px;
    margin-left: auto;
    margin-right: auto;
    width: 100%;
  }

  .step-indicator {
    color: var(--color-text-muted);
    font-size: var(--font-size-sm);
  }
</style>
