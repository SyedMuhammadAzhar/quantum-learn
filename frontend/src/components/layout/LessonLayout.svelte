<script>
  import './lessonLayout.css';
  import {
    lessonStore,
    currentLesson,
    currentStep,
    lessonProgress,
  } from "../../stores/lessonStore.js";
  import Button from "../ui/Button.svelte";
  
  // Import lesson components
  import SuperpositionStepContent from "../lessons/superposition/StepContent.svelte";
  import EntanglementStepContent from "../lessons/entanglement/StepContent.svelte";
  import MeasurementStepContent from "../lessons/measurement/StepContent.svelte";

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
        <!-- Render appropriate lesson content based on current lesson ID -->
        {#if $currentLesson.id === 'superposition'}
          <SuperpositionStepContent />
        {:else if $currentLesson.id === 'entanglement'}
          <EntanglementStepContent />
        {:else if $currentLesson.id === 'measurement'}
          <MeasurementStepContent />
        {:else}
          <div class="no-content">
            <h2>Lesson content not available</h2>
            <p>This lesson is under construction.</p>
          </div>
        {/if}
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
