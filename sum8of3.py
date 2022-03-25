# c0 = 1, c1 = 2, c2 = 3, c3 = 4, c4 = 5
# choose 3 numbers. The sum has to be 8
# generic aaproach: num = 3, sum = 8
# objectiv = (c0 x0 + c1 x1 + c2 x2 + c3 x3 + c4 x4 - sum)2 = 0, sum = 8
# objectiv = ((c0 - 2 sum) c0 x0 + (c1 - 2 sum) c1 x1 + (c2 - 2 sum) c2 x2 + (c3 - 2 sum) c3 x3 + (c4 - 2 sum) c4 x4 + 2 c0 c1 x0 x1 + 2 c0 c2 x0 x2 + 2 c0 c3 x0 x3 +
#             + 2 c0 c4 x0 x4 + + 2 c1 c2 x1 x2 + 2 c1 c3 x1 x3 + 2 c1 c4 x1 x4 + 2 c2 c3 x2 x3 + 2 c2 c4 x2 x4 + 2 c3 c4 x3 x4 + sum2
#
#
#
# constraint = (x0 + x1 + x2 + x3 + x4 - num)2 = 0, num = 3
# constraint = ((1 - 2 num) x0 + (1 - 2 num) x1 + (1 - 2 num) x2 + (1 - 2 num) x3 x2 + (1 - 2 num) x4 + 2 x0 x1 + 2 x0 x2 + 2 x0 x3 + 2 x0 x4
#               + 2 x1 x2 + 2 x1 x3 + 2 x1 x4 + 2 x2 x3 + 2 x2 x4 + 2 x3 x4 + num 2
# gamma = 1
# QUBO = min((c0 c0 - 2 c0 sum + 1 - 2 num) x0 + (c1 c1 - 2 c1 sum + 1 - 2 num) x1 + (c2 c2 - 2 c2 sum + 1 - 2 num) x2 + (c3 c3 - 2 c3 sum + 1 - 2 num) x3)
#          + (c4 c4 - 2 c4 sum + 1 - 2 num) x4 + (2 c0 c1 + 2) x0 x1 + (2 c0 c2 + 2) x0 x2 + (2 c0 c3 + 2) x0 x3 + (2 c0 c4 + 2) x0 x4
#          + (2 c1 c2 + 2) x1 x2 + (2 c1 c3 + 2) x1 x3 + (2 c1 c4 + 2) x1 x4 + (2 c2 c3 + 2) x2 x3 + (2 c2 c4 + 2) x2 x4 + (2 c0 c1 + 2) x3 x4
# QUBO = min (- 20 x0 - 33 x1 - 44 x2 - 53 x3 - 60 x4 + 6 x0 x1 + 8 x0 x2 + 10 x0 x3 + 12 x0 x4 + 14 x1 x2 + 18 x1 x3 + 22 x1 x4 + 26 x2 x3 + 32 x2 x4 + 42 x3 x4
# runs on the exact solver
# import
import dimod
# assign variable exactsolver
exactsolver = dimod.ExactSolver()
# QUBO a0 = -20, a1 = -33, a2 = -44, a3 = - 53, a4 = - 60, b01 = 6, b02 = 8 and b03 = 10, b04 = 12, b12 = 14, b13 = 18, b14 = 22, b23 = 26, b24 = 32, b34 = 42
Q = {(0,0):-20,(1,1):-33,(2,2):-44,(3,3):-53,(4,4):-60,(0,1):6,(0,2):8,(0,3):10,(0,4):12,(1,2):14,(1,3):18,(1,4):22,(2,3):26,(2,4):32,(3,4):42}
# assign results
results = exactsolver.sample_qubo(Q)
# print results
for sample, energy in (results.data(['sample', 'energy'])):
  print(sample, energy)
