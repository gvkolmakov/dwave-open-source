# German Kolmakov, City University of New York, 2023
# Testing D-Wave code with various solvers
# This code has MIT license
# Email gkolmakov@citytech.cuny.edu with any questions
#
# Testing of the hybrid solver for arbitrary number of qubits.
# Set N_QUBTS to the number you need.

import numpy as np
from dwave.system import EmbeddingComposite, DWaveSampler, LeapHybridSampler
from dimod.core.sampler import Sampler
from dimod.reference.samplers.identity_sampler import IdentitySampler
import dimod


import random
from math import log10, floor

def round_sig(x, sig=2):
    return round(x, sig-int(floor(log10(abs(x))))-1)


N_QUBTS = 5000

Q = {}

#linear part
for i in range(N_QUBTS):
    Q[( str(i), str(i) )] = round_sig(2.*random.random()-1.)
    
#quadratic part
for i in range(N_QUBTS-1):
    for j in range(i+1,N_QUBTS):
        Q[( str(i), str(j) )] = round_sig(2.*random.random()-1.)

sampler=LeapHybridSampler()
sample_set=sampler.sample_qubo(Q)
print(sample_set)

