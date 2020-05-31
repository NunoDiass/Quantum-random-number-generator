from quantumdevice import QuantumDevice
from simulator import SimulatedQubit, SimulatedQuantumDevice

def qrng(device: QuantumDevice) -> bool:
    with device.using_qubit() as q:
        q.h()
        return q.measure()
    
if __name__ == "__main__":
    qsim = SimulatedQuantumDevice()
    for idx_sample in range(10):
        random_sample = qrng(qsim)
        print(f"Our QRNG return {random_sample}.")