const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

/**
 * Custom error class for API errors
 */
class ApiError extends Error {
    constructor(message, status, data) {
        super(message);
        this.name = 'ApiError';
        this.status = status;
        this.data = data;
    }
}

/**
 * Base fetch wrapper with error handling
 */
async function fetchApi(endpoint, options = {}) {
    const url = `${API_BASE_URL}${endpoint}`;
    
    const defaultOptions = {
        headers: {
            'Content-Type': 'application/json',
        },
    };
    
    const mergedOptions = {
        ...defaultOptions,
        ...options,
        headers: {
            ...defaultOptions.headers,
            ...options.headers,
        },
    };
    
    try {
        const response = await fetch(url, mergedOptions);
        
        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new ApiError(
                errorData.detail || `HTTP error! status: ${response.status}`,
                response.status,
                errorData
            );
        }
        
        return await response.json();
    } catch (error) {
        if (error instanceof ApiError) {
            throw error;
        }
        
        // Network error or other fetch error
        throw new ApiError(
            'Network error: Unable to connect to the server. Make sure the backend is running.',
            0,
            { originalError: error.message }
        );
    }
}

/**
 * Quantum Coin Flip API
 */
export const quantumCoinApi = {
    /**
     * Perform a single quantum coin flip
     * @returns {Promise<{result: number, result_label: string}>}
     */
    flipOnce: () => fetchApi('/api/quantum-coin-flip', { method: 'POST' }),
    
    /**
     * Perform multiple quantum coin flips
     * @param {number} shots - Number of flips (1-10000)
     * @returns {Promise<{total_shots: number, zeros: number, ones: number, zero_percentage: number, one_percentage: number}>}
     */
    flipBatch: (shots = 100) => fetchApi('/api/quantum-coin-flip-batch', {
        method: 'POST',
        body: JSON.stringify({ shots }),
    }),
    
    /**
     * Get the quantum circuit diagram
     * @returns {Promise<{circuit_diagram: string}>}
     */
    getCircuit: () => fetchApi('/api/quantum-circuit'),
};

/**
 * Health check API
 */
export const healthApi = {
    /**
     * Check if the backend is running
     * @returns {Promise<{message: string, status: string}>}
     */
    check: () => fetchApi('/'),
};

// Future APIs will be added here:
// export const superpositionApi = { ... }
// export const entanglementApi = { ... }