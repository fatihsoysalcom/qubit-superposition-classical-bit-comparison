import random

class Qubit:
    """
    A simplified representation of a quantum bit (qubit).
    Unlike classical bits, qubits can exist in a superposition
    of 0 and 1 simultaneously, represented here by probabilities.
    """
    def __init__(self, prob_0: float, prob_1: float):
        # Ensure probabilities sum to approximately 1
        if not (0.99 <= prob_0 + prob_1 <= 1.01):
            raise ValueError("Probabilities must sum to 1")
        if not (0 <= prob_0 <= 1 and 0 <= prob_1 <= 1):
            raise ValueError("Probabilities must be between 0 and 1")

        self.prob_0 = prob_0
        self.prob_1 = prob_1

    def measure(self) -> int:
        """
        Simulates the measurement of a qubit, collapsing its superposition
        into a definite classical state (0 or 1) based on its probabilities.
        """
        # When measured, the qubit collapses to either 0 or 1.
        # The likelihood of collapsing to 0 is prob_0, and to 1 is prob_1.
        if random.random() < self.prob_0:
            return 0
        else:
            return 1

    def __str__(self):
        return f"Qubit (P(0)={self.prob_0:.2f}, P(1)={self.prob_1:.2f})"


def main():
    print("--- Classical Bit vs. Quantum Qubit ---")
    print("\nClassical Bit:")
    # A classical bit is always definitively 0 or 1.
    classical_bit = 0
    print(f"A classical bit is either {classical_bit} or 1. It cannot be both simultaneously.")
    print(f"Value after 'measurement': {classical_bit}")

    print("\nQuantum Qubit (Superposition):")
    # A qubit in superposition can be thought of as having a probability
    # of being 0 and a probability of being 1 until measured.
    # This specific qubit is in an equal superposition (50% chance for 0, 50% for 1).
    superposition_qubit = Qubit(0.5, 0.5)
    print(f"Initial state: {superposition_qubit}")
    print("Before measurement, a qubit can exist as both 0 and 1 simultaneously (superposition).")

    print("\nMeasuring the superposition qubit 10 times:")
    measurements = [superposition_qubit.measure() for _ in range(10)]
    print(f"Measurements: {measurements}")
    print(f"Count of 0s: {measurements.count(0)}, Count of 1s: {measurements.count(1)}")
    print("Notice how each measurement yields a definite 0 or 1, but the outcomes are probabilistic.")

    print("\n--- Relevance to Bitcoin Security ---")
    print("The article discusses how quantum computers, leveraging qubits and superposition,")
    print("could potentially break Bitcoin's cryptographic security (e.g., using Shor's algorithm).")
    print("The ability of qubits to explore multiple possibilities simultaneously allows quantum")
    print("computers to solve certain problems exponentially faster than classical computers.")
    print("IonQ's analysis suggests that around 20,000 'logical' qubits might be sufficient for this.")
    print("This example illustrates the fundamental difference in how information is processed.")

if __name__ == "__main__":
    main()
