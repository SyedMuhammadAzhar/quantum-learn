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
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # Svelte dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request/Response Models
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


class CircuitResponse(BaseModel):
    circuit_diagram: str


# API Endpoints
@app.get("/")
def root():
    return {"message": "QuantumLearn API is running", "status": "healthy"}


@app.post("/api/quantum-coin-flip", response_model=CoinFlipResponse)
def flip_quantum_coin():
    """
    Perform a single quantum coin flip.
    Uses Hadamard gate to create superposition, then measures.
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
    if request.shots < 1:
        request.shots = 1
    if request.shots > 10000:
        request.shots = 10000
    
    return quantum_service.quantum_coin_flip_batch(request.shots)


@app.get("/api/quantum-circuit", response_model=CircuitResponse)
def get_circuit():
    """
    Get the quantum circuit diagram for the coin flip.
    """
    diagram = quantum_service.get_circuit_diagram()
    return {"circuit_diagram": diagram}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)