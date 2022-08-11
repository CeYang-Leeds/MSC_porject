# qubit number=4
# total number=70
import pyquil
from pyquil.api import local_forest_runtime, QVMConnection
from pyquil import Program, get_qc
from pyquil.gates import *
import numpy as np

conn = QVMConnection()

def make_circuit()-> Program:

    prog = Program() # circuit begin



    prog += CNOT(0,1) # number=1
    prog += H(1) # number=22
    prog += S(1) # number=43
    prog += T(1) # number=44
    prog += T(1) # number=56
    prog += H(1) # number=45
    prog += CNOT(0,1) # number=23
    prog += H(0) # number=2
    prog += CZ(2,0) # number=46
    prog += H(0) # number=47
    prog += CNOT(2,0) # number=24
    prog += Z(2) # number=57
    prog += CNOT(2,0) # number=58
    prog += H(0) # number=25
    prog += CZ(2,0) # number=59
    prog += H(0) # number=60
    prog += H(3)  # number=3
    prog += T(3) # number=4
    prog += T(3) # number=26
    prog += T(3) # number=11
    prog += T(3) # number=27
    prog += RX(-2.0420352248333655,0) # number=5
    prog += H(0) # number=6
    prog += H(0) # number=12
    prog += CNOT(1,0) # number=28
    prog += H(0) # number=29
    prog += H(0) # number=13
    prog += CNOT(0,1) # number=1
    prog += H(1) # number=14
    prog += CZ(0,1) # number=48
    prog += H(1) # number=49
    prog += H(1) # number=30
    prog += CZ(0,1) # number=61
    prog += H(1) # number=62
    prog += X(1) # number=50
    prog += CNOT(0,1) # number=51
    prog += H(1) # number=31
    prog += CZ(0,1) # number=63
    prog += H(1) # number=64
    prog += CNOT(0,1) # number=15
    prog += H(0) # number=7
    prog += H(0) # number=32
    prog += CNOT(1,0) # number=52
    prog += H(0) # number=53
    prog += H(0) # number=33
    prog += H(0) # number=16
    prog += H(0) # number=34
    prog += CNOT(1,0) # number=65
    prog += H(0) # number=66
    prog += H(0) # number=35
    prog += CNOT(1,0) # number=17
    prog += H(2) # number=8
    prog += CZ(0,2) # number=36
    prog += H(2) # number=37
    prog += H(2) # number=18
    prog += S(2) # number=38
    prog += S(2) # number=39
    prog += H(2) # number=40
    prog += H(2) # number=19
    prog += H(2) # number=54
    prog += CNOT(0,2) # number=67
    prog += H(2) # number=68
    prog += H(2) # number=55
    prog += H(2) # number=9
    prog += H(2) # number=20
    prog += H(2) # number=41
    prog += CZ(3,2) # number=69
    prog += H(2) # number=70
    prog += H(2) # number=42
    prog += H(2) # number=21
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

    writefile = open("startPyquil_statevector_225.csv","w")
    print(state.get_outcome_probs(),file=writefile)
    writefile.close()
