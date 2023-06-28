# German Kolmakov, City University of New York, 2023
# Testing D-Wave code with various solvers
# This code has MIT license
# Email gkolmakov@citytech.cuny.edu with any questions

import numpy as np
from dwave.system import EmbeddingComposite, DWaveSampler, LeapHybridSampler
from dimod.core.sampler import Sampler
from dimod.reference.samplers.identity_sampler import IdentitySampler
import dimod


Q = { ('a', 'a'): -16., ('b', 'b'): -10., ('c', 'c'): -8.,  ('d', 'd'): -6.,     ('a', 'b'): 8., ('c', 'd'): 8. }

sampler=LeapHybridSampler()
sample_set=sampler.sample_qubo(Q)
print(sample_set)

#(Q, num_reads=100)
#save sample_set as python list


