# qubit number=4
# total number=20
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
    prog += T(3) # number=5
    prog += T(3) # number=15
    prog += S(3) # number=10
    prog += H(0) # number=6
    prog += CZ(1,0) # number=11
    prog += H(0) # number=12
    prog += CNOT(2,3) # number=7
    prog += CNOT(2,3) # number=16
    prog += CNOT(2,3) # number=17
    prog += CNOT(0,2) # number=8
    prog += H(2) # number=13
    prog += S(2) # number=18
    prog += S(2) # number=19
    prog += H(2) # number=20
    prog += CNOT(0,2) # number=14
    prog += X(2) # number=9
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
    writefile = open("startPyquil217.csv","w")
    print(summrise_results(bitstrings),file=writefile)
    writefile.close()

