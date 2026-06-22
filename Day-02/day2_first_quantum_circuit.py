from qiskit import QuantumCircuit
from qiskit_aer import Aer

qc = QuantumCircuit(1, 1)

qc.h(0)

qc.measure(0, 0)

simulator = Aer.get_backend('aer_simulator')

job = simulator.run(qc, shots=1000)

result = job.result()
counts = result.get_counts()

print(counts)