<script>
  import { chatStore } from "../../stores/chatStore.js";
  import { currentStep } from "../../stores/lessonStore.js";
  import { sendMessage, questionSuggestions } from "../../services/groqApi.js";
  import Button from "../ui/Button.svelte";

  let inputValue = $state("");
  let messagesContainer = $state(null);

  // Get suggestions based on current step
  let suggestions = $derived(
    $currentStep ? questionSuggestions[$currentStep.id] || [] : []
  );

  async function handleSend() {
    if (!inputValue.trim() || $chatStore.isLoading) return;

    const userMessage = inputValue.trim();
    inputValue = "";

    chatStore.addUserMessage(userMessage);
    chatStore.setLoading(true);

    try {
      const context = $currentStep
        ? `${$currentStep.title} - ${$currentStep.type}`
        : "";
      const response = await sendMessage($chatStore.messages, context);
      chatStore.addAssistantMessage(response);
    } catch (error) {
      chatStore.setError(error.message);
    }

    // Scroll to bottom
    setTimeout(() => {
      if (messagesContainer) {
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
      }
    }, 100);
  }

  function handleSuggestion(suggestion) {
    inputValue = suggestion;
    handleSend();
  }

  function handleKeydown(event) {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      handleSend();
    }
  }
</script>

<!-- Chat Toggle Button -->
<button class="chat-toggle" onclick={() => chatStore.toggleChat()}>
  {#if $chatStore.isOpen}
    ✕
  {:else}
    🤖
  {/if}
  {#if !$chatStore.isOpen}
    <span class="chat-label">Ask AI Tutor</span>
  {/if}
</button>

<!-- Chat Window -->
{#if $chatStore.isOpen}
  <div class="chat-window">
    <div class="chat-header">
      <div class="chat-title">
        <span class="chat-icon">🤖</span>
        <span>Quantum Tutor</span>
      </div>
      <button class="close-btn" onclick={() => chatStore.closeChat()}>✕</button>
    </div>

    <div class="chat-messages" bind:this={messagesContainer}>
      {#if $chatStore.messages.length === 0}
        <div class="welcome-message">
          <p>👋 Hi! I'm your quantum tutor.</p>
          <p>
            Ask me anything about the lesson, or try one of these questions:
          </p>

          {#if suggestions.length > 0}
            <div class="suggestions">
              {#each suggestions as suggestion}
                <button
                  class="suggestion-btn"
                  onclick={() => handleSuggestion(suggestion)}
                >
                  {suggestion}
                </button>
              {/each}
            </div>
          {/if}
        </div>
      {:else}
        {#each $chatStore.messages as message}
          <div class="message {message.role}">
            <div class="message-avatar">
              {message.role === "user" ? "👤" : "🤖"}
            </div>
            <div class="message-content">
              {message.content}
            </div>
          </div>
        {/each}

        {#if $chatStore.isLoading}
          <div class="message assistant">
            <div class="message-avatar">🤖</div>
            <div class="message-content typing">
              <span class="dot"></span>
              <span class="dot"></span>
              <span class="dot"></span>
            </div>
          </div>
        {/if}
      {/if}

      {#if $chatStore.error}
        <div class="error-message">
          ⚠️ {$chatStore.error}
        </div>
      {/if}
    </div>

    <div class="chat-input">
      <input
        type="text"
        placeholder="Type your question..."
        bind:value={inputValue}
        onkeydown={handleKeydown}
        disabled={$chatStore.isLoading}
      />
      <Button
        variant="primary"
        size="sm"
        onclick={handleSend}
        loading={$chatStore.isLoading}
        disabled={!inputValue.trim() || $chatStore.isLoading}
      >
        Send
      </Button>
    </div>
  </div>
{/if}

<style>
  .chat-toggle {
    position: fixed;
    bottom: var(--spacing-lg);
    right: var(--spacing-lg);
    background: var(--color-primary);
    color: white;
    border: none;
    border-radius: var(--radius-full);
    padding: var(--spacing-md);
    font-size: 24px;
    cursor: pointer;
    box-shadow: var(--shadow-lg);
    display: flex;
    align-items: center;
    gap: var(--spacing-sm);
    transition:
      transform var(--transition-fast),
      background var(--transition-fast);
    z-index: 1000;
  }

  .chat-toggle:hover {
    transform: scale(1.1);
    background: var(--color-primary-dark);
  }

  .chat-label {
    font-size: var(--font-size-sm);
    font-weight: 600;
  }

  .chat-window {
    position: fixed;
    bottom: 80px;
    right: var(--spacing-lg);
    width: 380px;
    height: 500px;
    background: var(--color-surface);
    border-radius: var(--radius-xl);
    box-shadow: var(--shadow-lg);
    display: flex;
    flex-direction: column;
    z-index: 999;
    overflow: hidden;
  }

  .chat-header {
    background: var(--color-primary);
    color: white;
    padding: var(--spacing-md);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .chat-title {
    display: flex;
    align-items: center;
    gap: var(--spacing-sm);
    font-weight: 600;
  }

  .chat-icon {
    font-size: 20px;
  }

  .close-btn {
    background: none;
    border: none;
    color: white;
    font-size: 20px;
    cursor: pointer;
    padding: var(--spacing-xs);
  }

  .chat-messages {
    flex: 1;
    overflow-y: auto;
    padding: var(--spacing-md);
    display: flex;
    flex-direction: column;
    gap: var(--spacing-md);
  }

  .welcome-message {
    text-align: center;
    color: var(--color-text-secondary);
    padding: var(--spacing-md);
  }

  .welcome-message p {
    margin: 0 0 var(--spacing-sm) 0;
  }

  .suggestions {
    display: flex;
    flex-direction: column;
    gap: var(--spacing-xs);
    margin-top: var(--spacing-md);
  }

  .suggestion-btn {
    background: var(--color-background);
    border: 1px solid var(--color-border);
    border-radius: var(--radius-md);
    padding: var(--spacing-sm);
    cursor: pointer;
    font-size: var(--font-size-sm);
    text-align: left;
    transition: background var(--transition-fast);
  }

  .suggestion-btn:hover {
    background: var(--color-border);
  }

  .message {
    display: flex;
    gap: var(--spacing-sm);
    align-items: flex-start;
  }

  .message.user {
    flex-direction: row-reverse;
  }

  .message-avatar {
    font-size: 20px;
    flex-shrink: 0;
  }

  .message-content {
    background: var(--color-background);
    padding: var(--spacing-sm) var(--spacing-md);
    border-radius: var(--radius-md);
    font-size: var(--font-size-sm);
    line-height: 1.5;
    max-width: 80%;
  }

  .message.user .message-content {
    background: var(--color-primary);
    color: white;
  }

  .typing {
    display: flex;
    gap: 4px;
    padding: var(--spacing-md);
  }

  .dot {
    width: 8px;
    height: 8px;
    background: var(--color-text-muted);
    border-radius: 50%;
    animation: bounce 1.4s infinite ease-in-out;
  }

  .dot:nth-child(2) {
    animation-delay: 0.2s;
  }

  .dot:nth-child(3) {
    animation-delay: 0.4s;
  }

  @keyframes bounce {
    0%,
    80%,
    100% {
      transform: scale(0);
    }
    40% {
      transform: scale(1);
    }
  }

  .error-message {
    background: #fff3cd;
    color: #856404;
    padding: var(--spacing-sm);
    border-radius: var(--radius-md);
    font-size: var(--font-size-sm);
  }

  .chat-input {
    padding: var(--spacing-md);
    border-top: 1px solid var(--color-border);
    display: flex;
    gap: var(--spacing-sm);
  }

  .chat-input input {
    flex: 1;
    padding: var(--spacing-sm);
    border: 1px solid var(--color-border);
    border-radius: var(--radius-md);
    font-size: var(--font-size-sm);
    font-family: inherit;
  }

  .chat-input input:focus {
    outline: none;
    border-color: var(--color-primary);
  }
</style>
