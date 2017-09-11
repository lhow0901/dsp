import sys
import os
import numpy as np

A = np.matrix([[1, 2, 3],[2, 7, 4]])
B = np.matrix([[1, -1], [0, 1]])
C = np.matrix([[5, -1], [9, 1], [6, 0]])
D = np.matrix([[3, -2, -1], [1, 2, 3]])
u = np.array([6, 2, -3, 5])
v = np.array([3, 5, -1, 4])
w = np.array([[1], [8],[0], [5]])

print("Q1 Answers")
print("1.1) Dimensions of A: ", A.shape)
print("1.2) Dimensions of B: ", B.shape)
print("1.3) Dimensions of C: ", C.shape)
print("1.4) Dimensions of D: ", D.shape)
print("1.5) Dimensions of u: ", u.shape)
print("1.6) Dimensions of w: ", w.shape)
print("1.7) Dimensions of v: ", v.shape, '\n')

print("Q2 Answers")
print("2.1) u - v = ", u - v)
print("2.2) u + v = ", u + v)
print("2.3) 6u = ", 6 * u)
print("2.4) u . v = ", np.dot(u, v))
print("2.5) ||u|| = ", abs(u), '\n')

print("Q3 Answers")
try:
    print("3.1) A + C = ", '\n', A + C)
except:
    print("3.1) A + C is not defined")
try:
    print("3.2) A - C^T = ", '\n', A - C.transpose())
except:
    print("3.2) A - C^T is not defined")
try:
    print("3.3) C^T + 3D = ", '\n', C.transpose() + (3 * D))
except:
    print("3.3) C^T + 3D is not defined")
try:
    print("3.4) BA = ", '\n', B * A)
except:
    print("3.4) BA is not defined")
try:
    print("3.5) BA^T = ", '\n', B * A.transpose())
except:
    print("3.5) BA^T is not defined")
try:
    print("3.6) BC = ", '\n', B * C)
except:
    print("3.6) BC is not defined")
try:
    print("3.7) CB = ", '\n', C * B)
except:
    print("3.7) CB is not defined")
try:
    print("3.8) B^4 = ", '\n', B ** 4)
except:
    print("3.8) B^4 is not defined")
try:
    print("3.9) AA^T = ", '\n', A * A.transpose())
except:
    print("3.9) AA^T is not defined")
try:
    print("3.10) D^T * D = ", '\n', D.transpose() * D)
except:
    print("3.10) D^T * D is not defined", '\n')
