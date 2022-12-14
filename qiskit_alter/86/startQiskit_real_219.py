# qubit number=4
# total number=19

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
    prog.t(input_qubit[0]) # number=4
    prog.t(input_qubit[0]) # number=17
    prog.t(input_qubit[0]) # number=10
    prog.t(input_qubit[0]) # number=18
    prog.y(input_qubit[1]) # number=5
    prog.y(input_qubit[3]) # number=6
    prog.h(input_qubit[2]) # number=7
    prog.cx(input_qubit[3],input_qubit[0]) # number=8
    prog.cx(input_qubit[3],input_qubit[0]) # number=11
    prog.s(input_qubit[3]) # number=13
    prog.s(input_qubit[3]) # number=19
    prog.cx(input_qubit[3],input_qubit[0]) # number=14
    prog.h(input_qubit[0]) # number=12
    prog.cz(input_qubit[3],input_qubit[0]) # number=15
    prog.h(input_qubit[0]) # number=16

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
    writefile = open("startQiskit_real_219.csv", "w", encoding="utf-8")
    IBMQ.load_account() 
    provider = IBMQ.get_provider(hub='ibm-q') 
    provider.backends()
    backend = least_busy(provider.backends(filters=lambda x: x.configuration().n_qubits >= 2 and not x.configuration().simulator and x.status().operational == True))

    circuit1 = transpile(prog, FakeYorktown())
    circuit1.measure_all()
    prog = circuit1

    info = execute(prog,backend=backend, shots=sample_shot).result().get_counts()

    print(info, file=writefile)
    print("results end", file=writefile)
    print(circuit1.depth(), file=writefile)
    print(circuit1, file=writefile)
    writefile.close()
