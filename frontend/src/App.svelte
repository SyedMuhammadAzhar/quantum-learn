<script>
  import { lessonStore, currentLesson } from "./stores/lessonStore.js";
  import LandingPage from "./components/layout/LandingPage.svelte";
  import LessonLayout from "./components/layout/LessonLayout.svelte";
  import ChatAssistant from "./components/layout/ChatAssistant.svelte";
  import SuperpositionStepContent from "./components/lessons/superposition/StepContent.svelte";
</script>

<div class="app">
  {#if $currentLesson}
    <!-- In a lesson -->
    <LessonLayout>
      {#if $currentLesson.id === "superposition"}
        <SuperpositionStepContent />
      {/if}
    </LessonLayout>

    <!-- AI Chat Assistant (only in lessons) -->
    <ChatAssistant />
  {:else}
    <!-- Landing page -->
    <div class="landing-wrapper">
      <LandingPage />

      <footer class="app-footer">
        <p>Built with Qiskit + FastAPI + Svelte | TÖL031M Final Project</p>
      </footer>
    </div>
  {/if}
</div>

<style>
  .app {
    min-height: 100vh;
  }

  .landing-wrapper {
    min-height: 100vh;
    background: linear-gradient(
      135deg,
      var(--color-primary) 0%,
      var(--color-primary-dark) 100%
    );
    padding: var(--spacing-xl);
  }

  .app-footer {
    text-align: center;
    color: white;
    margin-top: var(--spacing-2xl);
    opacity: 0.8;
  }

  .app-footer p {
    margin: var(--spacing-xs) 0;
  }

  .team {
    font-weight: 600;
    letter-spacing: 2px;
  }
</style>
