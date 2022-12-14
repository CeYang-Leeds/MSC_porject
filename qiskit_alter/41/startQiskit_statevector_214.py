# qubit number=4
# total number=13

import numpy as np
from qiskit.providers.ibmq import least_busy
from qiskit import QuantumCircuit, execute, Aer, QuantumRegister, ClassicalRegister, transpile, BasicAer, IBMQ
import networkx as nx
from qiskit.visualization import plot_histogram
from typing import *
from pprint import pprint
from math import log2
from collections import Counter
from qiskit.test.mock import FakeVigo, FakeYorktown
from qiskit.providers.aer import QasmSimulator

kernel = 'circuit/bernstein'


def make_circuit(n:int) -> QuantumCircuit:
    # circuit begin
    input_qubit = QuantumRegister(n,"qc")
    prog = QuantumCircuit(input_qubit)
    prog.h(input_qubit[0]) # number=1
    prog.rx(0.87687634,input_qubit[1]) # number=2
    prog.t(input_qubit[0]) # number=3
    prog.t(input_qubit[0]) # number=9
    prog.z(input_qubit[0]) # number=4
    prog.y(input_qubit[1]) # number=5
    prog.s(input_qubit[3]) # number=6
    prog.s(input_qubit[3]) # number=12
    prog.h(input_qubit[2]) # number=7
    prog.s(input_qubit[2]) # number=10
    prog.s(input_qubit[2]) # number=13
    prog.h(input_qubit[2]) # number=11
    prog.h(input_qubit[3])  # number=8

    for edge in E:
        k = edge[0]
        l = edge[1]
        prog.cp(-2 * gamma, input_qubit[k-1], input_qubit[l-1])
        prog.p(gamma, k)
        prog.p(gamma, l)

    prog.rx(2 * beta, range(len(V)))

    # circuit end



    return prog



if __name__ == '__main__':
    n = 4
    V = np.arange(0, n, 1)
    E = [(0, 1, 1.0), (0, 2, 1.0), (1, 2, 1.0), (3, 2, 1.0), (3, 1, 1.0)]

    G = nx.Graph()
    G.add_nodes_from(V)
    G.add_weighted_edges_from(E)

    step_size = 0.1

    a_gamma = np.arange(0, np.pi, step_size)
    a_beta = np.arange(0, np.pi, step_size)
    a_gamma, a_beta = np.meshgrid(a_gamma, a_beta)

    F1 = 3 - (np.sin(2 * a_beta) ** 2 * np.sin(2 * a_gamma) ** 2 - 0.5 * np.sin(4 * a_beta) * np.sin(4 * a_gamma)) * (
                1 + np.cos(4 * a_gamma) ** 2)

    result = np.where(F1 == np.amax(F1))
    a = list(zip(result[0], result[1]))[0]

    gamma = a[0] * step_size
    beta = a[1] * step_size

    prog = make_circuit(4)
    sample_shot =5600
    writefile = open("startQiskit_statevector_214.csv", "w", encoding="utf-8")
    backend = BasicAer.get_backend('statevector_simulator')

    circuit1 = transpile(prog, FakeYorktown())
    prog = circuit1

    info = execute(prog,backend=backend, shots=sample_shot).result().get_counts()

    print(info, file=writefile)
    print("results end", file=writefile)
    print(circuit1.depth(), file=writefile)
    print(circuit1, file=writefile)
    writefile.close()
