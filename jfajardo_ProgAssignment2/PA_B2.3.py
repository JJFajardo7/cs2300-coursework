# Name: Jesse Fajardo
# Class: CS2300

import sympy as sp

#gets input for the flows from the user
flow1 = int(input('Enter flow1: '))
flow2 = int(input('Enter flow2: '))
flow3 = int(input('Enter flow3: '))
flow4 = int(input('Enter flow4: '))


#creates the mat with the flows
mat1 = sp.Matrix([[1, 0, 1, 0, 0, 0, 0, flow1], 
                [1, -1, 0, -1, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 0, 0, flow2]
                [0, 0, 1, 0, 0, 1, 0, flow3],
                [0, 0, 0, 1, 0, -1, 1, 0],
                [0, 0, 0, 0, 1, 0, 1, flow4]])

print("The flow mat: ")
print(mat1)

#gets the reduced form
m_rref, pivots = mat1.rref()

print("The reduced mat: ")
sp.pprint(m_rref)

print("\nSolutions:")
symbols = sp.symbols('x1 x2 x3 x4 x5 x6 x7')
for i, row in enumerate(m_rref.tolist()):
    equation = sum(row[j] * symbols[j] for j in range(7)) - row[7]
    sp.pprint(sp.Eq(equation, 0))
