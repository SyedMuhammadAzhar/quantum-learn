from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from quantum_service import quantum_service

app = FastAPI(
    title="QuantumLearn API",
    description="Backend API for quantum computing education platform",
    version="1.0.0"
)

# Allow frontend to connect (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:3000",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==================== Request/Response Models ====================

class BatchFlipRequest(BaseModel):
    shots: int = 100


class CoinFlipResponse(BaseModel):
    result: int
    result_label: str


class BatchFlipResponse(BaseModel):
    total_shots: int
    zeros: int
    ones: int
    zero_percentage: float
    one_percentage: float
    theoretical_probability: float


class DoubleCoinFlipResponse(BaseModel):
    result: str
    coin1: int
    coin2: int
    coin1_label: str
    coin2_label: str


class DoubleBatchFlipResponse(BaseModel):
    total_shots: int
    counts: dict
    percentages: dict
    labels: dict
    theoretical_probability: float


class CircuitResponse(BaseModel):
    circuit_diagram: str


# ==================== Bell State Models ====================

class BellStateRequest(BaseModel):
    state: str  # phi_plus, psi_plus, phi_minus, psi_minus


class BellStateBatchRequest(BaseModel):
    state: str
    shots: int = 100


class BellStateResponse(BaseModel):
    result: str
    state: str
    description: str


class BellStateBatchResponse(BaseModel):
    counts: dict
    total_shots: int
    state: str
    percentages: dict
    expected_percentages: dict
    description: str


# ==================== Measurement Models ====================

class MeasureQubitRequest(BaseModel):
    state: str  # equal, biased_0, biased_1, definite_0, definite_1
    basis: str = "z"  # z or x


class MeasureQubitBatchRequest(BaseModel):
    state: str
    basis: str = "z"
    shots: int = 100


class MeasureQubitResponse(BaseModel):
    result: str
    state: str
    basis: str


class MeasureQubitBatchResponse(BaseModel):
    counts: dict
    total_shots: int
    state: str
    basis: str
    percentages: dict


# ==================== Health Check ====================

@app.get("/")
def root():
    """Health check endpoint."""
    return {
        "message": "QuantumLearn API is running",
        "status": "healthy",
        "version": "1.0.0",
        "available_endpoints": {
            "superposition": [
                "/api/quantum-coin-flip",
                "/api/quantum-coin-flip-batch",
                "/api/double-coin-flip",
                "/api/double-coin-flip-batch"
            ],
            "entanglement": [
                "/api/bell-state-measure",
                "/api/bell-state-batch",
                "/api/bell-states/info"
            ],
            "measurement": [
                "/api/measure-qubit",
                "/api/measure-qubit-batch"
            ],
            "docs": "/docs"
        }
    }


# ==================== SINGLE COIN ENDPOINTS (1 Qubit) ====================

@app.post("/api/quantum-coin-flip", response_model=CoinFlipResponse)
def flip_quantum_coin():
    """
    Perform a single quantum coin flip.
    
    Uses Hadamard gate to create superposition:
    - H|0⟩ = (|0⟩ + |1⟩) / √2
    - 50% chance of 0 (Heads), 50% chance of 1 (Tails)
    """
    result = quantum_service.quantum_coin_flip()
    return {
        "result": result,
        "result_label": "Heads" if result == 0 else "Tails"
    }


@app.post("/api/quantum-coin-flip-batch", response_model=BatchFlipResponse)
def flip_quantum_coin_batch(request: BatchFlipRequest):
    """
    Perform multiple quantum coin flips at once.
    Returns statistics showing convergence to 50/50.
    """
    # Validate shots range
    shots = max(1, min(request.shots, 10000))
    return quantum_service.quantum_coin_flip_batch(shots)


@app.get("/api/quantum-circuit", response_model=CircuitResponse)
def get_single_circuit():
    """Get the quantum circuit diagram for single coin flip."""
    diagram = quantum_service.get_single_circuit_diagram()
    return {"circuit_diagram": diagram}


# ==================== DOUBLE COIN ENDPOINTS (2 Qubits) ====================

@app.post("/api/double-coin-flip", response_model=DoubleCoinFlipResponse)
def flip_double_coin():
    """
    Perform a double quantum coin flip (2 qubits).
    
    Uses Hadamard gates on both qubits:
    - H|0⟩ ⊗ H|0⟩ = (|00⟩ + |01⟩ + |10⟩ + |11⟩) / 2
    - 25% chance for each outcome: 00, 01, 10, 11
    """
    return quantum_service.double_coin_flip()


@app.post("/api/double-coin-flip-batch", response_model=DoubleBatchFlipResponse)
def flip_double_coin_batch(request: BatchFlipRequest):
    """
    Perform multiple double quantum coin flips at once.
    Returns statistics for all 4 possible outcomes.
    """
    # Validate shots range
    shots = max(1, min(request.shots, 10000))
    return quantum_service.double_coin_flip_batch(shots)


@app.get("/api/double-quantum-circuit", response_model=CircuitResponse)
def get_double_circuit():
    """Get the quantum circuit diagram for double coin flip."""
    diagram = quantum_service.get_double_circuit_diagram()
    return {"circuit_diagram": diagram}


# ==================== BELL STATE ENDPOINTS (Entanglement) ====================

@app.post("/api/bell-state-measure", response_model=BellStateResponse)
def measure_bell_state(request: BellStateRequest):
    """
    Measure a Bell state once and return the result.
    
    Bell states are maximally entangled two-qubit states:
    - phi_plus: Φ⁺ = (|00⟩ + |11⟩)/√2 - Qubits always match
    - psi_plus: Ψ⁺ = (|01⟩ + |10⟩)/√2 - Qubits always differ
    - phi_minus: Φ⁻ = (|00⟩ - |11⟩)/√2 - Qubits match (phase)
    - psi_minus: Ψ⁻ = (|01⟩ - |10⟩)/√2 - Qubits differ (phase)
    """
    try:
        return quantum_service.bell_state_measure(request.state)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/api/bell-state-batch", response_model=BellStateBatchResponse)
def measure_bell_state_batch(request: BellStateBatchRequest):
    """
    Measure a Bell state multiple times and return statistics.
    Shows quantum correlations over many measurements.
    """
    # Validate shots range
    shots = max(1, min(request.shots, 10000))
    try:
        return quantum_service.bell_state_batch(request.state, shots)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/api/bell-states/info")
def get_bell_states_info():
    """
    Get information about all available Bell states.
    Useful for the frontend to display state options.
    """
    return {
        "bell_states": {
            "phi_plus": {
                "name": "Φ⁺",
                "formula": "(|00⟩ + |11⟩)/√2",
                "description": "Both qubits always match",
                "correlations": "00 or 11 (50% each)"
            },
            "psi_plus": {
                "name": "Ψ⁺",
                "formula": "(|01⟩ + |10⟩)/√2",
                "description": "Both qubits always differ",
                "correlations": "01 or 10 (50% each)"
            },
            "phi_minus": {
                "name": "Φ⁻",
                "formula": "(|00⟩ - |11⟩)/√2",
                "description": "Both qubits match (opposite phase)",
                "correlations": "00 or 11 (50% each)"
            },
            "psi_minus": {
                "name": "Ψ⁻",
                "formula": "(|01⟩ - |10⟩)/√2",
                "description": "Both qubits differ (opposite phase)",
                "correlations": "01 or 10 (50% each)"
            }
        }
    }


# ==================== MEASUREMENT ENDPOINTS ====================

@app.post("/api/measure-qubit", response_model=MeasureQubitResponse)
def measure_qubit(request: MeasureQubitRequest):
    """
    Measure a prepared quantum state in a chosen basis.
    
    Demonstrates wavefunction collapse and Born rule.
    
    States:
    - equal: (|0⟩ + |1⟩)/√2 - 50/50 superposition
    - biased_0: (√3|0⟩ + |1⟩)/2 - 75% for 0
    - biased_1: (|0⟩ + √3|1⟩)/2 - 75% for 1
    - definite_0: |0⟩ - always 0
    - definite_1: |1⟩ - always 1
    
    Bases:
    - z: Computational basis (standard 0 or 1)
    - x: Hadamard basis (+ or -)
    """
    try:
        return quantum_service.measure_qubit(request.state, request.basis)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/api/measure-qubit-batch", response_model=MeasureQubitBatchResponse)
def measure_qubit_batch(request: MeasureQubitBatchRequest):
    """
    Measure a quantum state multiple times to observe probability distribution.
    
    Shows Born Rule in action: P(outcome) = |amplitude|²
    """
    shots = max(1, min(request.shots, 10000))
    try:
        return quantum_service.measure_qubit_batch(request.state, request.basis, shots)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# ==================== Run Server ====================

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting QuantumLearn API server...")
    print("📍 API docs available at: http://localhost:8000/docs")
    print("📚 Lessons: Superposition ✅ | Entanglement ✅ | Measurement ✅")
    uvicorn.run(app, host="0.0.0.0", port=8000)