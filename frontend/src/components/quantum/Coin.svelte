<script>
  import { onMount, onDestroy } from "svelte";
  import { gsap } from "gsap";

  let { isSpinning = false, result = null } = $props();

  let coinElement = $state(null);
  let spinTimeline = null; // Not reactive - just a reference

  onMount(() => {
    if (isSpinning && coinElement) {
      startSpinning();
    }
  });

  onDestroy(() => {
    if (spinTimeline) {
      spinTimeline.kill();
    }
  });

  $effect(() => {
    // Only react to isSpinning changes, not internal state
    const spinning = isSpinning;

    if (coinElement) {
      if (spinning) {
        startSpinning();
      } else {
        stopSpinning();
      }
    }
  });

  function startSpinning() {
    if (spinTimeline) {
      spinTimeline.kill();
    }

    if (!coinElement) return;

    spinTimeline = gsap.to(coinElement, {
      rotationY: "+=360",
      duration: 0.8,
      ease: "none",
      repeat: -1,
    });
  }

  function stopSpinning() {
    if (spinTimeline) {
      spinTimeline.kill();
      spinTimeline = null;
    }
  }

  export function animateCollapse(newResult) {
    return new Promise((resolve) => {
      if (spinTimeline) {
        spinTimeline.kill();
        spinTimeline = null;
      }

      if (!coinElement) {
        resolve();
        return;
      }

      const finalRotation = newResult === 0 ? 0 : 180;

      gsap.to(coinElement, {
        rotationY: finalRotation,
        duration: 0.5,
        ease: "power2.out",
        onComplete: resolve,
      });
    });
  }

  export function animateBatch() {
    return new Promise((resolve) => {
      if (spinTimeline) {
        spinTimeline.kill();
        spinTimeline = null;
      }

      if (!coinElement) {
        resolve();
        return;
      }

      gsap.to(coinElement, {
        rotationY: "+=3600",
        duration: 2,
        ease: "power2.inOut",
        onComplete: resolve,
      });
    });
  }

  export function resetPosition() {
    return new Promise((resolve) => {
      if (!coinElement) {
        resolve();
        return;
      }

      gsap.to(coinElement, {
        rotationY: 0,
        duration: 0.3,
        onComplete: resolve,
      });
    });
  }
</script>

<div class="coin-wrapper">
  <div class="coin" bind:this={coinElement}>
    <div class="coin-face heads">
      <span class="coin-symbol">H</span>
      <span class="coin-state">|0⟩</span>
    </div>
    <div class="coin-face tails">
      <span class="coin-symbol">T</span>
      <span class="coin-state">|1⟩</span>
    </div>
  </div>
</div>

<style>
  .coin-wrapper {
    perspective: 1000px;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: var(--spacing-xl);
  }

  .coin {
    width: 150px;
    height: 150px;
    position: relative;
    transform-style: preserve-3d;
    cursor: pointer;
  }

  .coin-face {
    position: absolute;
    width: 100%;
    height: 100%;
    border-radius: 50%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    backface-visibility: hidden;
    box-shadow: var(--shadow-lg);
  }

  .coin-symbol {
    font-size: var(--font-size-4xl);
    font-weight: 700;
    color: white;
  }

  .coin-state {
    font-size: var(--font-size-sm);
    color: rgba(255, 255, 255, 0.8);
    font-family: "Courier New", monospace;
  }

  .heads {
    background: linear-gradient(
      135deg,
      var(--color-heads),
      var(--color-heads-light)
    );
  }

  .tails {
    background: linear-gradient(
      135deg,
      var(--color-tails),
      var(--color-tails-light)
    );
    transform: rotateY(180deg);
  }
</style>
