# qubit number=4
# total number=29
import pyquil
from pyquil.api import local_forest_runtime, QVMConnection
from pyquil import Program, get_qc
from pyquil.gates import *
import numpy as np

conn = QVMConnection()

def make_circuit()-> Program:

    prog = Program() # circuit begin



    prog += H(1)  # number=1
    prog += Z(2)  # number=2
    prog += H(3)  # number=3
    prog += Y(3) # number=4
    prog += CNOT(3,0) # number=10
    prog += CNOT(3,0) # number=12
    prog += Z(3) # number=17
    prog += CNOT(3,0) # number=18
    prog += CNOT(3,0) # number=13
    prog += H(0) # number=5
    prog += CZ(1,0) # number=19
    prog += H(0) # number=20
    prog += SWAP(2,3) # number=6
    prog += H(2) # number=7
    prog += T(2) # number=14
    prog += T(2) # number=21
    prog += S(2) # number=15
    prog += H(2) # number=16
    prog += H(2) # number=9
    prog += CZ(3,2) # number=24
    prog += H(2) # number=25
    prog += Z(3) # number=11
    prog += H(2) # number=8
    prog += CZ(0,2) # number=26
    prog += H(2) # number=27
    prog += CNOT(0,2) # number=22
    prog += X(2) # number=28
    prog += CNOT(0,2) # number=29
    prog += CNOT(0,2) # number=23
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

    writefile = open("startPyquil_statevector_216.csv","w")
    print(state.get_outcome_probs(),file=writefile)
    writefile.close()
