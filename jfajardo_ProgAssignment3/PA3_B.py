# Name: Jesse Fajardo
# Class: CS2300

import sympy as sp
import numpy as np

file1Name = input("Enter file 1 name: ")
inputMessage = np.loadtxt(file1Name).astype(float)
colSize2 = inputMessage.size

inputList = inputMessage.tolist()

print(inputList)

#creates the mat with the flows
mat1 = sp.Matrix([[1, -1, 1, 0],
                [-1, 1, -1, 0],
                [inputList[0], inputList[1], 0, inputList[4]],
                [0, inputList[2], inputList[3], inputList[5]]])

print("The flow mat: ")
print(mat1)

#gets the reduced form
m_rref, pivots = mat1.rref()

print("The reduced mat: ")
sp.pprint(m_rref)

i1 = round(m_rref[0,3], 2)
i2 = round(m_rref[1,3], 2)
i3 = round(m_rref[2,3], 2)
i4 = round(m_rref[3,3], 2)

print("i1 = %.2f" %i1,
"i2 = %.2f" %i2,
"i3 = %.2f" %i3,
"i4 = %.2f" %i4)
