import numpy as np
from quantumdevice import Qubit, QuantumDevice

KET_0 = np.array([
    [1],
    [0]
], dtype=complex)

H = np.array([
    [1,1],
    [1, -1]
], dtype=complex) / np.sqrt(2)

class SimulatedQubit(Qubit):
    def __init__(self):
        self.reset()
    
    def h(self):
        self.state = H @ self.state
    
    def measure(self) -> bool:
        pr0 = np.abs(self.state[0,0]) ** 2
        sample = np.random.random() <= pr0
        return bool(0 if sample else 1)
    
    def reset(self):
        self.state = KET_0.copy()

class SimulatedQuantumDevice(QuantumDevice):
    def allocate_qubit(self):
        return SimulatedQubit()
    
    def deallocate_qubit(self, qubit):
        qubit = None

    