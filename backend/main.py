from fastapi import FastAPI
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


# ==================== Health Check ====================

@app.get("/")
def root():
    """Health check endpoint."""
    return {
        "message": "QuantumLearn API is running",
        "status": "healthy",
        "version": "1.0.0"
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


# ==================== Run Server ====================

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting QuantumLearn API server...")
    print("📍 API docs available at: http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)