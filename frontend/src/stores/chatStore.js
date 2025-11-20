import { writable } from 'svelte/store';

function createChatStore() {
    const { subscribe, set, update } = writable({
        messages: [],
        isLoading: false,
        isOpen: false,
        error: null
    });

    return {
        subscribe,
        
        toggleChat: () => update(state => ({
            ...state,
            isOpen: !state.isOpen
        })),
        
        openChat: () => update(state => ({
            ...state,
            isOpen: true
        })),
        
        closeChat: () => update(state => ({
            ...state,
            isOpen: false
        })),
        
        addUserMessage: (content) => update(state => ({
            ...state,
            messages: [...state.messages, {
                role: 'user',
                content,
                timestamp: Date.now()
            }]
        })),
        
        addAssistantMessage: (content) => update(state => ({
            ...state,
            messages: [...state.messages, {
                role: 'assistant',
                content,
                timestamp: Date.now()
            }],
            isLoading: false
        })),
        
        setLoading: (loading) => update(state => ({
            ...state,
            isLoading: loading
        })),
        
        setError: (error) => update(state => ({
            ...state,
            error,
            isLoading: false
        })),
        
        clearError: () => update(state => ({
            ...state,
            error: null
        })),
        
        clearMessages: () => update(state => ({
            ...state,
            messages: [],
            error: null
        })),
        
        reset: () => set({
            messages: [],
            isLoading: false,
            isOpen: false,
            error: null
        })
    };
}

export const chatStore = createChatStore();