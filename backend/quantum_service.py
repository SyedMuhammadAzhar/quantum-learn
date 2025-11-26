from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from typing import Dict


class QuantumService:
    """
    Quantum computing service using Qiskit for quantum demonstrations.
    Implements:
    - Superposition: Hadamard gates for coin flip simulations
    - Entanglement: Bell states for quantum correlation demonstrations
    - Measurement: Different states and bases to demonstrate wavefunction collapse
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
    
    # ==================== BELL STATES (Entanglement) ====================
    
    def create_bell_state(self, state_type: str) -> QuantumCircuit:
        """
        Create different Bell states using quantum gates.
        
        Bell states are maximally entangled two-qubit states:
        - Φ⁺ = (|00⟩ + |11⟩)/√2  → H on q0, CNOT(q0, q1)
        - Ψ⁺ = (|01⟩ + |10⟩)/√2  → X on q1, H on q0, CNOT(q0, q1)
        - Φ⁻ = (|00⟩ - |11⟩)/√2  → H on q0, CNOT(q0, q1), Z on q0
        - Ψ⁻ = (|01⟩ - |10⟩)/√2  → X on q1, H on q0, CNOT(q0, q1), Z on q0
        
        Args:
            state_type: One of "phi_plus", "psi_plus", "phi_minus", "psi_minus"
            
        Returns:
            QuantumCircuit ready for measurement
        """
        qc = QuantumCircuit(2, 2)
        
        if state_type == "phi_plus":
            # Φ⁺ = (|00⟩ + |11⟩)/√2
            # Circuit: H on q0, then CNOT with q0 as control
            qc.h(0)      # Create superposition on qubit 0
            qc.cx(0, 1)  # Entangle qubit 0 with qubit 1
        
        elif state_type == "psi_plus":
            # Ψ⁺ = (|01⟩ + |10⟩)/√2
            # Circuit: Flip q1, then H on q0, then CNOT
            qc.x(1)      # Flip qubit 1 to |1⟩
            qc.h(0)      # Create superposition on qubit 0
            qc.cx(0, 1)  # Entangle
        
        elif state_type == "phi_minus":
            # Φ⁻ = (|00⟩ - |11⟩)/√2
            # Circuit: H on q0, CNOT, then Z on q0 (adds phase)
            qc.h(0)      # Create superposition
            qc.cx(0, 1)  # Entangle
            qc.z(0)      # Add phase to create minus state
        
        elif state_type == "psi_minus":
            # Ψ⁻ = (|01⟩ - |10⟩)/√2
            # Circuit: X on q1, H on q0, CNOT, Z on q0
            qc.x(1)      # Flip qubit 1
            qc.h(0)      # Create superposition
            qc.cx(0, 1)  # Entangle
            qc.z(0)      # Add phase
        
        else:
            raise ValueError(f"Unknown Bell state: {state_type}. Must be one of: phi_plus, psi_plus, phi_minus, psi_minus")
        
        # Measure both qubits
        qc.measure([0, 1], [0, 1])
        
        return qc
    
    def bell_state_measure(self, state_type: str) -> Dict:
        """
        Measure a Bell state once and return the result.
        
        Args:
            state_type: One of "phi_plus", "psi_plus", "phi_minus", "psi_minus"
            
        Returns:
            Dict with result and state information
        """
        qc = self.create_bell_state(state_type)
        
        # Run circuit once
        result = self.simulator.run(qc, shots=1).result()
        counts = result.get_counts()
        
        # Get the single measurement result
        measurement = list(counts.keys())[0]
        
        return {
            "result": measurement,
            "state": state_type,
            "description": self._get_bell_state_description(state_type)
        }
    
    def bell_state_batch(self, state_type: str, shots: int = 100) -> Dict:
        """
        Measure a Bell state multiple times and return statistics.
        
        Args:
            state_type: One of "phi_plus", "psi_plus", "phi_minus", "psi_minus"
            shots: Number of measurements (1-10000)
            
        Returns:
            Dict with counts, percentages, and expected values
        """
        qc = self.create_bell_state(state_type)
        
        # Run circuit multiple times
        result = self.simulator.run(qc, shots=shots).result()
        counts = result.get_counts()
        
        # Ensure all possible outcomes are in the result
        all_outcomes = {"00": 0, "01": 0, "10": 0, "11": 0}
        all_outcomes.update(counts)
        
        # Get expected probabilities for this Bell state
        expected = self._get_expected_probabilities(state_type)
        
        return {
            "counts": all_outcomes,
            "total_shots": shots,
            "state": state_type,
            "percentages": {
                outcome: round((count / shots) * 100, 2)
                for outcome, count in all_outcomes.items()
            },
            "expected_percentages": {
                outcome: prob * 100
                for outcome, prob in expected.items()
            },
            "description": self._get_bell_state_description(state_type)
        }
    
    def _get_expected_probabilities(self, state_type: str) -> Dict[str, float]:
        """Get theoretical probabilities for each Bell state."""
        probabilities = {
            "phi_plus": {"00": 0.5, "01": 0.0, "10": 0.0, "11": 0.5},
            "psi_plus": {"00": 0.0, "01": 0.5, "10": 0.5, "11": 0.0},
            "phi_minus": {"00": 0.5, "01": 0.0, "10": 0.0, "11": 0.5},
            "psi_minus": {"00": 0.0, "01": 0.5, "10": 0.5, "11": 0.0}
        }
        return probabilities.get(state_type, {"00": 0.25, "01": 0.25, "10": 0.25, "11": 0.25})
    
    def _get_bell_state_description(self, state_type: str) -> str:
        """Get human-readable description of Bell state."""
        descriptions = {
            "phi_plus": "Φ⁺ = (|00⟩ + |11⟩)/√2 - Both qubits always match",
            "psi_plus": "Ψ⁺ = (|01⟩ + |10⟩)/√2 - Both qubits always differ",
            "phi_minus": "Φ⁻ = (|00⟩ - |11⟩)/√2 - Both qubits match (opposite phase)",
            "psi_minus": "Ψ⁻ = (|01⟩ - |10⟩)/√2 - Both qubits differ (opposite phase)"
        }
        return descriptions.get(state_type, "Unknown Bell state")
    
    def get_bell_state_circuit_diagram(self, state_type: str) -> str:
        """Get text representation of Bell state circuit."""
        qc = self.create_bell_state(state_type)
        return qc.draw(output='text').single_string()
    
    # ==================== MEASUREMENT (Different States & Bases) ====================
    
    def measure_qubit(self, state: str, basis: str = "z") -> Dict:
        """
        Measure a prepared quantum state in a chosen basis.
        
        States:
        - equal: (|0⟩ + |1⟩)/√2 - 50/50 superposition
        - biased_0: (√3|0⟩ + |1⟩)/2 - 75% for 0
        - biased_1: (|0⟩ + √3|1⟩)/2 - 75% for 1
        - definite_0: |0⟩ - always 0
        - definite_1: |1⟩ - always 1
        
        Bases:
        - z: Computational basis (0 or 1)
        - x: Hadamard basis (+ or -)
        
        Returns:
            Dict with result and state information
        """
        qc = QuantumCircuit(1, 1)
        
        # Prepare the state
        if state == "equal":
            qc.h(0)  # Equal superposition
        elif state == "biased_0":
            # (√3|0⟩ + |1⟩)/2
            qc.ry(2 * 0.5236, 0)  # arcsin(1/2) ≈ 0.5236
        elif state == "biased_1":
            # (|0⟩ + √3|1⟩)/2
            qc.ry(2 * 1.0472, 0)  # arcsin(√3/2) ≈ 1.0472
        elif state == "definite_0":
            pass  # Already |0⟩
        elif state == "definite_1":
            qc.x(0)  # Flip to |1⟩
        else:
            raise ValueError(f"Unknown state: {state}")
        
        # Apply measurement basis rotation
        if basis == "x":
            qc.h(0)  # Rotate to X-basis
        elif basis != "z":
            raise ValueError(f"Unknown basis: {basis}")
        
        # Measure
        qc.measure(0, 0)
        
        # Run circuit
        result = self.simulator.run(qc, shots=1).result()
        counts = result.get_counts()
        measurement = list(counts.keys())[0]
        
        return {
            "result": measurement,
            "state": state,
            "basis": basis
        }
    
    def measure_qubit_batch(self, state: str, basis: str = "z", shots: int = 100) -> Dict:
        """
        Measure a quantum state multiple times to see probability distribution.
        
        Args:
            state: One of equal, biased_0, biased_1, definite_0, definite_1
            basis: "z" or "x"
            shots: Number of measurements
            
        Returns:
            Dict with counts and probabilities
        """
        qc = QuantumCircuit(1, 1)
        
        # Prepare the state
        if state == "equal":
            qc.h(0)
        elif state == "biased_0":
            qc.ry(2 * 0.5236, 0)
        elif state == "biased_1":
            qc.ry(2 * 1.0472, 0)
        elif state == "definite_0":
            pass
        elif state == "definite_1":
            qc.x(0)
        else:
            raise ValueError(f"Unknown state: {state}")
        
        # Apply measurement basis rotation
        if basis == "x":
            qc.h(0)
        elif basis != "z":
            raise ValueError(f"Unknown basis: {basis}")
        
        # Measure
        qc.measure(0, 0)
        
        # Run circuit
        result = self.simulator.run(qc, shots=shots).result()
        counts = result.get_counts()
        
        # Ensure both outcomes are present
        all_counts = {"0": 0, "1": 0}
        all_counts.update(counts)
        
        return {
            "counts": all_counts,
            "total_shots": shots,
            "state": state,
            "basis": basis,
            "percentages": {
                "0": round((all_counts["0"] / shots) * 100, 2),
                "1": round((all_counts["1"] / shots) * 100, 2)
            }
        }


# Create singleton instance
quantum_service = QuantumService()