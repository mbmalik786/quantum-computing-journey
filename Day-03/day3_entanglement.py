from qiskit import QuantumCircuit
from qiskit_aer import Aer

# Create a quantum circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Apply Hadamard gate to qubit 0
qc.h(0)

# Apply CNOT gate
# Qubit 0 = control, Qubit 1 = target
qc.cx(0, 1)

# Measure both qubits
qc.measure([0, 1], [0, 1])

# Use Aer simulator
simulator = Aer.get_backend('aer_simulator')

# Run the circuit 1000 times
job = simulator.run(qc, shots=1000)

# Get result
result = job.result()
counts = result.get_counts()

# Print output
print(counts)