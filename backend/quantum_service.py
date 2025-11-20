from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from typing import Dict


class QuantumService:
    """
    Quantum computing service using Qiskit for coin flip simulations.
    Implements Hadamard gates for creating superposition states.
    """
    
    def __init__(self):
        self.simulator = AerSimulator()
    
    # ==================== SINGLE COIN FLIP (1 Qubit) ====================
    
    def quantum_coin_flip(self) -> int:
        """
        Simulate a single quantum coin flip using Hadamard gate.
        
        Circuit:
            |0⟩ ─[H]─ M ─→ 0 or 1
        
        The Hadamard gate creates equal superposition:
            H|0⟩ = (|0⟩ + |1⟩) / √2
        
        This gives 50% probability for each outcome.
        
        Returns:
            int: 0 (heads) or 1 (tails)
        """
        # Create quantum circuit: 1 qubit, 1 classical bit
        qc = QuantumCircuit(1, 1)
        
        # Apply Hadamard gate to create superposition
        # |0⟩ → (|0⟩ + |1⟩) / √2
        qc.h(0)
        
        # Measure the qubit (collapses superposition)
        qc.measure(0, 0)
        
        # Run circuit once
        result = self.simulator.run(qc, shots=1).result()
        counts = result.get_counts()
        
        # Return 0 or 1
        return 0 if '0' in counts else 1
    
    def quantum_coin_flip_batch(self, shots: int = 100) -> Dict:
        """
        Run multiple quantum coin flips at once.
        
        Args:
            shots: Number of measurements (1-10000)
            
        Returns:
            Dict with counts and percentages
        """
        qc = QuantumCircuit(1, 1)
        qc.h(0)
        qc.measure(0, 0)
        
        result = self.simulator.run(qc, shots=shots).result()
        counts = result.get_counts()
        
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
    
    def get_single_circuit_diagram(self) -> str:
        """Get text representation of single coin flip circuit."""
        qc = QuantumCircuit(1, 1)
        qc.h(0)
        qc.measure(0, 0)
        return qc.draw(output='text').single_string()
    
    # ==================== DOUBLE COIN FLIP (2 Qubits) ====================
    
    def double_coin_flip(self) -> Dict:
        """
        Simulate a double quantum coin flip using Hadamard gates on 2 qubits.
        
        Circuit:
            q0: |0⟩ ─[H]─ M ─┐
                              ├─→ 00, 01, 10, or 11
            q1: |0⟩ ─[H]─ M ─┘
        
        Each qubit independently goes into superposition:
            H|0⟩ ⊗ H|0⟩ = (|0⟩ + |1⟩)/√2 ⊗ (|0⟩ + |1⟩)/√2
                        = (|00⟩ + |01⟩ + |10⟩ + |11⟩) / 2
        
        This gives 25% probability for each of the 4 outcomes.
        
        Returns:
            Dict with result string and individual coin values
        """
        # Create quantum circuit: 2 qubits, 2 classical bits
        qc = QuantumCircuit(2, 2)
        
        # Apply Hadamard gate to BOTH qubits (independent superposition)
        qc.h(0)  # Qubit 0: |0⟩ → (|0⟩ + |1⟩) / √2
        qc.h(1)  # Qubit 1: |0⟩ → (|0⟩ + |1⟩) / √2
        
        # Measure both qubits
        qc.measure(0, 0)  # Measure qubit 0 into classical bit 0
        qc.measure(1, 1)  # Measure qubit 1 into classical bit 1
        
        # Run circuit once
        result = self.simulator.run(qc, shots=1).result()
        counts = result.get_counts()
        
        # Get result string (Qiskit returns in reverse bit order)
        result_str = list(counts.keys())[0]
        
        # Parse individual coins
        # Qiskit bit order: result_str[0] = qubit 1, result_str[1] = qubit 0
        coin1 = int(result_str[1])  # First coin (qubit 0)
        coin2 = int(result_str[0])  # Second coin (qubit 1)
        
        return {
            "result": f"{coin1}{coin2}",
            "coin1": coin1,
            "coin2": coin2,
            "coin1_label": "Heads" if coin1 == 0 else "Tails",
            "coin2_label": "Heads" if coin2 == 0 else "Tails"
        }
    
    def double_coin_flip_batch(self, shots: int = 100) -> Dict:
        """
        Run multiple double quantum coin flips at once.
        
        Args:
            shots: Number of measurements (1-10000)
            
        Returns:
            Dict with counts and percentages for all 4 outcomes
        """
        qc = QuantumCircuit(2, 2)
        qc.h(0)
        qc.h(1)
        qc.measure(0, 0)
        qc.measure(1, 1)
        
        result = self.simulator.run(qc, shots=shots).result()
        counts = result.get_counts()
        
        # Initialize all possible outcomes
        results = {"00": 0, "01": 0, "10": 0, "11": 0}
        
        # Parse results (handle Qiskit's reverse bit order)
        for key, count in counts.items():
            # Reverse the bit string to match our convention
            corrected_key = key[::-1]
            results[corrected_key] = count
        
        return {
            "total_shots": shots,
            "counts": results,
            "percentages": {
                "00": round((results["00"] / shots) * 100, 2),
                "01": round((results["01"] / shots) * 100, 2),
                "10": round((results["10"] / shots) * 100, 2),
                "11": round((results["11"] / shots) * 100, 2)
            },
            "labels": {
                "00": "Both Heads",
                "01": "H & T",
                "10": "T & H",
                "11": "Both Tails"
            },
            "theoretical_probability": 25.0
        }
    
    def get_double_circuit_diagram(self) -> str:
        """Get text representation of double coin flip circuit."""
        qc = QuantumCircuit(2, 2)
        qc.h(0)
        qc.h(1)
        qc.measure(0, 0)
        qc.measure(1, 1)
        return qc.draw(output='text').single_string()


# Create singleton instance
quantum_service = QuantumService()