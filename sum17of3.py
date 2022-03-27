# c0 = 1, c1 = 2, c2 = 5, c3 = 7, c4 = 10, c5 = 11
# choose 3 numbers. The sum has to be 17
# sulution 1: c0 + c2 + c5 = 1 + 5 + 11 = 17
# sulution 2: c1 + c2 + c4 = 2 + 5 + 10 = 17
# generic aaproach: num = 3, sum = 17
# objectiv = (c0 x0 + c1 x1 + c2 x2 + c3 x3 + c4 x4 + c5 x5 - sum)2 = 0, sum = 17
# objectiv = ((c0 - 2 sum) c0 x0 + (c1 - 2 sum) c1 x1 + (c2 - 2 sum) c2 x2 + (c3 - 2 sum) c3 x3 + (c4 - 2 sum) c4 x4 + (c5 - 2 sum) c5 x5 + 2 c0 c1 x0 x1 + 2 c0 c2 x0 x2
#             + 2 c0 c3 x0 x3 + 2 c0 c4 x0 x4 + 2 c0 c5 x0 x5 + 2 c1 c2 x1 x2 + 2 c1 c3 x1 x3 + 2 c1 c4 x1 x4 + 2 c1 c5 x1 x5 + 2 c2 c3 x2 x3 + 2 c2 c4 x2 x4  + 2 c2 c5 x2 x5
#             + 2 c3 c4 x3 x4 + 2 c3 c5 x3 x5 + 2 c4 c5 x4 x5 + sum2
# constraint = (x0 + x1 + x2 + x3 + x4 - num)2 = 0, num = 3
# constraint = ((1 - 2 num) x0 + (1 - 2 num) x1 + (1 - 2 num) x2 + (1 - 2 num) x3 x2 + (1 - 2 num) x4 + (1 - 2 num) x5 + 2 x0 x1 + 2 x0 x2 + 2 x0 x3 + 2 x0 x4
#               + 2 x0 x5 + 2 x1 x2 + 2 x1 x3 + 2 x1 x4 + 2 x1 x5 + 2 x2 x3 + 2 x2 x4 + 2 x2 x5 + 2 x3 x4 + 2 x3 x5 + 2 x4 x5 + num 2
# gamma = 1
# QUBO = min((c0 c0 - 2 c0 sum + 1 - 2 num) x0 + (c1 c1 - 2 c1 sum + 1 - 2 num) x1 + (c2 c2 - 2 c2 sum + 1 - 2 num) x2 + (c3 c3 - 2 c3 sum + 1 - 2 num) x3)
#          + (c4 c4 - 2 c4 sum + 1 - 2 num) x4 + (c5 c5 - 2 c5 sum + 1 - 2 num) x5 + (2 c0 c1 + 2) x0 x1 + (2 c0 c2 + 2) x0 x2 + (2 c0 c3 + 2) x0 x3 + (2 c0 c4 + 2) x0 x4
#          + (2 c0 c5 + 2) x0 x5 + (2 c1 c2 + 2) x1 x2 + (2 c1 c3 + 2) x1 x3 + (2 c1 c4 + 2) x1 x4 + (2 c1 c5 + 2) x1 x5 + (2 c2 c3 + 2) x2 x3 + (2 c2 c4 + 2) x2 x4
#          + (2 c2 c5 + 2) x2 x5 + (2 c3 c4 + 2) x3 x4 + (2 c3 c5 + 2) x3 x5 + (2 c4 c5 + 2) x4 x5
# QUBO = min (- 38 x0 - 69 x1 - 150 x2 - 194 x3 - 245 x4 - 253 x5 + 6 x0 x1 + 12 x0 x2 + 14 x0 x3 + 22 x0 x4 + 24 x0 x5 + 22 x1 x2 + 30 x1 x3 + 42 x1 x4 + 46 x1 x5
              + 72 x2 x3 + 102 x2 x4 + 112 x2 x5 + 142 x3 x4 + 156 x3 x5 + 222 x4 x5
# runs on the exact solver
# import
import dimod
# assign variable exactsolver
exactsolver = dimod.ExactSolver()
# QUBO a0 = -38, a1 = -69, a2 = -150, a3 = -194, a4 = -245, a5 = -253, b01 = 6, b02 = 12, b03 = 14, b04 = 22, b05 = 24 b12 = 22, b13 = 30, b14 = 42, b15 = 46,
#      b23 = 72, b24 = 102, b25 = 112, b34 = 142, b35 = 156, b45 = 222
Q = {(0,0):-38,(1,1):-69,(2,2):-150,(3,3):-194,(4,4):-245,(5,5):-253,(0,1):6,(0,2):12,(0,3):14,(0,4):22,(0,5):24,(1,2):22,(1,3):30,(1,4):42,(1,5):46,\
     (2,3):72,(2,4):102,(2,5):112,(3,4):142,(3,5):156,(4,5):222}
# assign results
results = exactsolver.sample_qubo(Q)
# print results
for sample, energy in (results.data(['sample', 'energy'])):
  print(sample, energy)
