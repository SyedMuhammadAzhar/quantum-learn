<script>
  import './chatAssistant.css';
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
