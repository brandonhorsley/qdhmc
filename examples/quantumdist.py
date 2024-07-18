"""
This file is for comparing performance of QDHMC and classic HMC on a 'quantum' distribution, by this I mean evaluating performance on a probability distribution produced by an IQP circuit.

Notes/thoughts:
- QDHMC is a classical simulation of a quantum algorithm, so computational complexity/efficiency is pointless without running on quantum hardware
- Probability destribution is discrete, quasi-continuous in higher limits, perhaps a small modification to HMC to round to nearest tuple is warranted
- Get unitary matrix gate working by explicitly writing a random numpy matrix
"""

#Import modules
import sys
sys.path.append("..")

import cirq.circuits
import qdhmc
from qdhmc import HMC
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cirq
import scipy.stats

#Define IQP circuit
# H tensor N U tensor N H tensor N on |0> tensor N

N=4 #number of modes

q0, q1, q2, q3 = [cirq.GridQubit(i, 0) for i in range(N)]

circuit=cirq.Circuit()
#circuit.append([cirq.H(q0),cirq.H(q1), cirq.H(q2), cirq.H(q3), cirq.testing.random_unitary(dim=N), cirq.H(q0),cirq.H(q1), cirq.H(q2), cirq.H(q3)])
U=np.array(scipy.stats.unitary_group.rvs(N))
print(U)
circuit.append([cirq.H(q0),cirq.H(q1), cirq.H(q2), cirq.H(q3), cirq.MatrixGate(U), cirq.H(q0),cirq.H(q1), cirq.H(q2), cirq.H(q3)])

print(circuit) #test
#Run algs on this prob distribution

#Performance metrics (plots, convergence...etc)