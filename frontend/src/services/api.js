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
        
        // Network error
        throw new ApiError(
            'Network error: Unable to connect to the server. Make sure the backend is running on port 8000.',
            0,
            { originalError: error.message }
        );
    }
}

/**
 * Single Quantum Coin Flip API (1 Qubit)
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
     * @returns {Promise<{total_shots, zeros, ones, zero_percentage, one_percentage}>}
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
 * Double Quantum Coin Flip API (2 Qubits)
 */
export const doubleCoinApi = {
    /**
     * Perform a double quantum coin flip
     * @returns {Promise<{result, coin1, coin2, coin1_label, coin2_label}>}
     */
    flipOnce: () => fetchApi('/api/double-coin-flip', { method: 'POST' }),
    
    /**
     * Perform multiple double quantum coin flips
     * @param {number} shots - Number of flips (1-10000)
     * @returns {Promise<{total_shots, counts, percentages, labels}>}
     */
    flipBatch: (shots = 100) => fetchApi('/api/double-coin-flip-batch', {
        method: 'POST',
        body: JSON.stringify({ shots }),
    }),
    
    /**
     * Get the double quantum circuit diagram
     * @returns {Promise<{circuit_diagram: string}>}
     */
    getCircuit: () => fetchApi('/api/double-quantum-circuit'),
};

/**
 * Bell State (Entanglement) API
 */
export const bellStateApi = {
    /**
     * Measure a Bell state once
     * @param {string} state - Bell state type: phi_plus, psi_plus, phi_minus, psi_minus
     * @returns {Promise<{qubit1, qubit2, state, description}>}
     */
    measure: (state = 'phi_plus') => fetchApi('/api/bell-state-measure', {
        method: 'POST',
        body: JSON.stringify({ state }),
    }),
    
    /**
     * Perform multiple Bell state measurements
     * @param {string} state - Bell state type
     * @param {number} shots - Number of measurements (1-10000)
     * @returns {Promise<{total_measurements, counts, percentages, state, expected}>}
     */
    batchMeasure: (state = 'phi_plus', shots = 100) => fetchApi('/api/bell-state-batch', {
        method: 'POST',
        body: JSON.stringify({ state, shots }),
    }),
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