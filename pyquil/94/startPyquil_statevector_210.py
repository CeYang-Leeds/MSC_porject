# qubit number=4
# total number=22
import pyquil
from pyquil.api import local_forest_runtime, QVMConnection
from pyquil import Program, get_qc
from pyquil.gates import *
import numpy as np

conn = QVMConnection()

def make_circuit()-> Program:

    prog = Program() # circuit begin



    prog += H(1)  # number=1
    prog += RX(-0.38013271108436497,2) # number=11
    prog += CNOT(2,1) # number=14
    prog += CNOT(2,1) # number=15
    prog += CNOT(2,1) # number=16
    prog += RX(-0.24818581963359365,2) # number=10
    prog += RX(-0.38013271108436497,2) # number=11
    prog += CNOT(2,1) # number=14
    prog += CNOT(2,1) # number=17
    prog += CNOT(2,1) # number=18
    prog += Y(2) # number=2
    prog += H(3)  # number=3
    prog += Y(3) # number=4
    prog += CNOT(1,0) # number=5
    prog += CNOT(1,0) # number=6
    prog += CNOT(1,0) # number=19
    prog += CNOT(1,0) # number=20
    prog += RX(1.168672467135403,1) # number=12
    prog += CNOT(0,2) # number=7
    prog += X(2) # number=21
    prog += CNOT(0,2) # number=22
    prog += CNOT(1,2) # number=13
    prog += CNOT(3,2) # number=9
    prog += Z(2) # number=8
    # circuit end

    return prog

def summrise_results(bitstrings) -> dict:
    d = {}
    for l in bitstrings:
        if d.get(l) is None:
            d[l] = 1
        else:
            d[l] = d[l] + 1

    return d

if __name__ == '__main__':
    prog = make_circuit()
    state = conn.wavefunction(prog)

    writefile = open("startPyquil_statevector_210.csv","w")
    print(state.get_outcome_probs(),file=writefile)
    writefile.close()
