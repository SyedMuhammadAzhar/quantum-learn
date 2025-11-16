import { writable, derived } from 'svelte/store';

/**
 * Store for quantum coin flip statistics
 */
function createCoinFlipStore() {
    const { subscribe, set, update } = writable({
        totalFlips: 0,
        headsCount: 0,
        tailsCount: 0,
        history: [], // Last N results
        maxHistoryLength: 50,
    });
    
    return {
        subscribe,
        
        /**
         * Add a single flip result
         * @param {number} result - 0 for heads, 1 for tails
         */
        addFlip: (result) => update(state => {
            const newHistory = [...state.history, result].slice(-state.maxHistoryLength);
            return {
                ...state,
                totalFlips: state.totalFlips + 1,
                headsCount: state.headsCount + (result === 0 ? 1 : 0),
                tailsCount: state.tailsCount + (result === 1 ? 1 : 0),
                history: newHistory,
            };
        }),
        
        /**
         * Add batch flip results
         * @param {number} zeros - Number of heads
         * @param {number} ones - Number of tails
         */
        addBatch: (zeros, ones) => update(state => ({
            ...state,
            totalFlips: state.totalFlips + zeros + ones,
            headsCount: state.headsCount + zeros,
            tailsCount: state.tailsCount + ones,
            // Don't update history for batch (too many results)
        })),
        
        /**
         * Reset all statistics
         */
        reset: () => set({
            totalFlips: 0,
            headsCount: 0,
            tailsCount: 0,
            history: [],
            maxHistoryLength: 50,
        }),
    };
}

export const coinFlipStore = createCoinFlipStore();

/**
 * Derived store for percentages
 */
export const coinFlipPercentages = derived(coinFlipStore, ($store) => {
    const headsPercentage = $store.totalFlips > 0 
        ? (($store.headsCount / $store.totalFlips) * 100).toFixed(1)
        : '0.0';
    
    const tailsPercentage = $store.totalFlips > 0
        ? (($store.tailsCount / $store.totalFlips) * 100).toFixed(1)
        : '0.0';
    
    return {
        heads: parseFloat(headsPercentage),
        tails: parseFloat(tailsPercentage),
        headsFormatted: headsPercentage,
        tailsFormatted: tailsPercentage,
    };
});