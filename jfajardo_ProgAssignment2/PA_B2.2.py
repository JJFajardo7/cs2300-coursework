# Name: Jesse Fajardo
# Class: CS2300

import sympy as sp

#creates the mat with the flows
mat1 = sp.Matrix([[1, 0, 1, 0, 0, 0, 0, 600], 
                [1, -1, 0, -1, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 0, 0, 500],
                [0, 0, 1, 0, 0, 1, 0, 600],
                [0, 0, 0, 1, 0, -1, 1, 0],
                [0, 0, 0, 0, 1, 0, 1, 500]])

print("The flow mat: ")
sp.pprint(mat1)

#gets the reduced form
m_rref, pivots = mat1.rref()

print("The reduced mat: ")
sp.pprint(m_rref)

print("\nSolutions:")
symbols = sp.symbols('x1 x2 x3 x4 x5 x6 x7')
for i, row in enumerate(m_rref.tolist()):
    equation = sum(row[j] * symbols[j] for j in range(7)) - row[7]
    sp.pprint(sp.Eq(equation, 0))


