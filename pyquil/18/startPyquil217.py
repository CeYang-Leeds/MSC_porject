# qubit number=4
# total number=43
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
    prog += T(2) # number=2
    prog += T(2) # number=32
    prog += S(2) # number=13
    prog += H(3)  # number=3
    prog += Y(3) # number=4
    prog += H(0) # number=5
    prog += CZ(1,0) # number=33
    prog += H(0) # number=34
    prog += H(3) # number=12
    prog += H(0) # number=6
    prog += CZ(1,0) # number=26
    prog += H(0) # number=27
    prog += H(0) # number=14
    prog += H(0) # number=28
    prog += CNOT(1,0) # number=35
    prog += H(0) # number=36
    prog += H(0) # number=29
    prog += H(0) # number=15
    prog += CZ(1,0) # number=37
    prog += H(0) # number=38
    prog += H(2) # number=7
    prog += S(2) # number=16
    prog += T(2) # number=17
    prog += T(2) # number=23
    prog += H(2) # number=18
    prog += H(2) # number=9
    prog += CZ(3,2) # number=19
    prog += H(2) # number=20
    prog += H(0) # number=8
    prog += CZ(2,0) # number=39
    prog += H(0) # number=40
    prog += S(2) # number=21
    prog += S(2) # number=41
    prog += H(0) # number=22
    prog += H(0) # number=24
    prog += H(0) # number=30
    prog += CZ(2,0) # number=42
    prog += H(0) # number=43
    prog += H(0) # number=31
    prog += H(0) # number=25
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

