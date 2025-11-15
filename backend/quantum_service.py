from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from typing import Dict, List


class QuantumService:
    def __init__(self):
        self.simulator = AerSimulator()
    
    def quantum_coin_flip(self) -> int:
        """
        Simulate a single quantum coin flip using Hadamard gate.
        Returns 0 (heads) or 1 (tails).
        """
        # Create a quantum circuit with 1 qubit and 1 classical bit
        qc = QuantumCircuit(1, 1)
        
        # Apply Hadamard gate to create superposition: |0⟩ → (|0⟩ + |1⟩)/√2
        qc.h(0)
        
        # Measure the qubit
        qc.measure(0, 0)
        
        # Run the circuit once
        result = self.simulator.run(qc, shots=1).result()
        counts = result.get_counts()
        
        # Return 0 or 1 based on measurement
        return 0 if '0' in counts else 1
    
    def quantum_coin_flip_batch(self, shots: int = 100) -> Dict:
        """
        Run multiple quantum coin flips at once.
        Returns statistics about the results.
        """
        # Create circuit
        qc = QuantumCircuit(1, 1)
        qc.h(0)
        qc.measure(0, 0)
        
        # Run multiple shots
        result = self.simulator.run(qc, shots=shots).result()
        counts = result.get_counts()
        
        # Parse results
        zeros = counts.get('0', 0)
        ones = counts.get('1', 0)
        
        return {
            "total_shots": shots,
            "zeros": zeros,
            "ones": ones,
            "zero_percentage": round((zeros / shots) * 100, 2),
            "one_percentage": round((ones / shots) * 100, 2),
            "theoretical_probability": 50.0
        }
    
    def get_circuit_diagram(self) -> str:
        """
        Return a text representation of the quantum coin flip circuit.
        """
        qc = QuantumCircuit(1, 1)
        qc.h(0)
        qc.measure(0, 0)
        return qc.draw(output='text').single_string()


# Create a singleton instance
quantum_service = QuantumService()