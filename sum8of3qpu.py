# choose 3 numbers of 1,2,3,4,5
# the sum has to be 8
# solution 1: 1 + 2 + 5 = 8
# solution 2: 1 + 3 + 4 = 8
# energy is - 73
# import
from dwave.system import EmbeddingComposite, DWaveSampler
# QUBO a0 = -20, a1 = -33, a2 = -44, a3 = - 53, a4 = -60, b01 = 6, b02 = 8, b03 = 10, b04 = 12, b12 = 14, b13 = 18, b14 = 22, b23 = 26, b24 = 30, b34 = 42
Q = {(0,0):-20,(1,1):-33,(2, 2):-44,(3,3):-53,(4,4):-60,(0,1):6,(0,2):8,(0,3):10,(0,4):12,(1,2):14,(1,3):18,(1,4):22,(2,3):26,(2,4):30,(3,4):42}
# run embedding sampler
sampler = EmbeddingComposite(DWaveSampler())
# assign to sampleset
sampleset = sampler.sample_qubo(Q, num_reads = 10, label='Michaels Example - Smallest sum two of 7, 71, 29: QUBO')
# print
print(sampleset)
