<script>
  import QuantumCoinFlip from './components/quantum/QuantumCoinFlip.svelte';
</script>

<div class="app">
  <header class="app-header">
    <h1 class="app-title">🔬 QuantumLearn</h1>
    <p class="app-subtitle">Interactive Quantum Computing Education Platform</p>
  </header>
  
  <main class="app-main">
    <QuantumCoinFlip />
  </main>
  
  <footer class="app-footer">
    <p>Built with Qiskit + FastAPI + Svelte | TÖL031M Final Project</p>
    <p class="team">Azhar • Zahid • Kalsoom</p>
  </footer>
</div>

<style>
  .app {
    min-height: 100vh;
    background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-primary-dark) 100%);
    padding: var(--spacing-lg);
  }
  
  .app-header {
    text-align: center;
    color: white;
    margin-bottom: var(--spacing-xl);
  }
  
  .app-title {
    font-size: var(--font-size-4xl);
    margin: 0 0 var(--spacing-sm) 0;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
  }
  
  .app-subtitle {
    font-size: var(--font-size-lg);
    margin: 0;
    opacity: 0.9;
  }
  
  .app-main {
    max-width: 900px;
    margin: 0 auto;
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