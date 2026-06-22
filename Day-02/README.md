# 📅 Day 2 — First Quantum Circuit

## ✅ What I Did
- Installed Python and Qiskit
- Created my first quantum circuit
- Used quantum simulator Qiskit Aer
- Observed superposition behavior

---

## 🧠 Concepts Learned

### 🔹 Qubit
A qubit is a quantum bit.  
Unlike a classical bit, which can be only 0 or 1, a qubit can exist in a combination of both states before measurement.

### 🔹 Superposition
Superposition means a qubit can be in both 0 and 1 states at the same time.

In this circuit, I used the Hadamard gate to create superposition.

### 🔹 Hadamard Gate
The Hadamard gate is used to put a qubit into superposition.

```python
qc.h(0)
