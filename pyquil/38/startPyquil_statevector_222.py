# qubit number=4
# total number=32
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
    prog += RX(-0.24818581963359365,2) # number=10
    prog += RX(-0.38013271108436497,2) # number=11
    prog += Z(2)  # number=2
    prog += H(3)  # number=3
    prog += Y(3) # number=4
    prog += H(0) # number=5
    prog += H(0) # number=22
    prog += CNOT(1,0) # number=28
    prog += H(0) # number=29
    prog += H(0) # number=23
    prog += H(0) # number=6
    prog += CZ(1,0) # number=24
    prog += H(0) # number=25
    prog += CNOT(1,0) # number=16
    prog += H(0) # number=17
    prog += CZ(1,0) # number=30
    prog += H(0) # number=31
    prog += RX(1.168672467135403,1) # number=12
    prog += H(2) # number=7
    prog += T(2) # number=13
    prog += T(2) # number=18
    prog += S(2) # number=14
    prog += H(2) # number=15
    prog += H(2) # number=9
    prog += H(2) # number=20
    prog += CNOT(3,2) # number=26
    prog += H(2) # number=27
    prog += H(2) # number=21
    prog += S(2) # number=8
    prog += T(2) # number=19
    prog += T(2) # number=32
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

    writefile = open("startPyquil_statevector_222.csv","w")
    print(state.get_outcome_probs(),file=writefile)
    writefile.close()
