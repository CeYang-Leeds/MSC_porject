# qubit number=4
# total number=23
import pyquil
from pyquil.api import local_forest_runtime, QVMConnection
from pyquil import Program, get_qc
from pyquil.gates import *
import numpy as np

conn = QVMConnection()

def make_circuit()-> Program:

    prog = Program('PRAGMA INITIAL_REWIRING "NAIVE"') # circuit begin


    prog += H(1)  # number=1
    prog += H(0) # number=2
    prog += CZ(2,0) # number=18
    prog += H(0) # number=19
    prog += Z(2) # number=12
    prog += CNOT(2,0) # number=13
    prog += H(3)  # number=3
    prog += RX(-2.0420352248333655,0) # number=4
    prog += CNOT(2,3) # number=5
    prog += SWAP(1,0) # number=6
    prog += CNOT(2,0) # number=10
    prog += CNOT(2,0) # number=14
    prog += Z(2) # number=20
    prog += CNOT(2,0) # number=21
    prog += H(0) # number=15
    prog += CZ(2,0) # number=22
    prog += H(0) # number=23
    prog += CNOT(0,2) # number=7
    prog += X(2) # number=16
    prog += CNOT(0,2) # number=17
    prog += CNOT(3,2) # number=8
    prog += H(0) # number=11
    prog += Z(2) # number=9
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
    qvm = get_qc('4q-qvm')

    results = qvm.run_and_measure(prog,1024)
    bitstrings = np.vstack([results[i] for i in qvm.qubits()]).T
    bitstrings = [''.join(map(str, l)) for l in bitstrings]
    writefile = open("startPyquil_pragma_211.csv","w")
    print(summrise_results(bitstrings),file=writefile)
    writefile.close()
