# choose 3 numbers of 1,2,3,4,5
# the sum has to be 8
# solution 1: 1 + 2 + 5 = 8
# solution 2: 1 + 3 + 4 = 8
# energy is - 73
import dimod
from dwave.system import EmbeddingComposite, DWaveSampler
# define obj as quadratic model 
obj = BinaryQuadraticModel()
# QUBO a0 = -20, a1 = -33, a2 = -44, a3 = - 53, a4 = -60, b01 = 6, b02 = 8, b03 = 10, b04 = 12, b12 = 14, b13 = 18, b14 = 22, b23 = 26, b24 = 32, b34 = 42
# Q = {(0,0):-20,(1,1):-33,(2, 2):-44,(3,3):-53,(4,4):-60,(0,1):6,(0,2):8,(0,3):10,(0,4):12,(1,2):14,(1,3):18,(1,4):22,(2,3):26,(2,4):32,(3,4):42}
for i in range (5):
  obj.add_variable(i)
  print(i)
  
obj.set_linear(list(obj.linear.keys())[0],-20)
obj.set_linear(list(obj.linear.keys())[1],-33)
obj.set_linear(list(obj.linear.keys())[2],-44)
obj.set_linear(list(obj.linear.keys())[3],-53)
obj.set_linear(list(obj.linear.keys())[4],-60)
obj.set_quadratic(list(obj.quadratic.keys())[0,1],6)
obj.set_quadratic(list(obj.quadratic.keys())[0,2],8)
obj.set_quadratic(list(obj.quadratic.keys())[0,3],10)
obj.set_quadratic(list(obj.quadratic.keys())[0,4],12)
obj.set_quadratic(list(obj.quadratic.keys())[1,2],14)
obj.set_quadratic(list(obj.quadratic.keys())[1,3],18)
obj.set_quadratic(list(obj.quadratic.keys())[1,4],22)
obj.set_quadratic(list(obj.quadratic.keys())[2,3],26)
obj.set_quadratic(list(obj.quadratic.keys())[2,4],32)
obj.set_quadratic(list(obj.quadratic.keys())[3,4],42)
# run embedding sampler
sampler = EmbeddingComposite(DWaveSampler())
# assign to sampleset
sampleset = sampler.sample_qubo(obj, num_reads = 32, label='Michaels Example - sum 8 with 3 numbers: QUBO')
# print
print(sampleset)
