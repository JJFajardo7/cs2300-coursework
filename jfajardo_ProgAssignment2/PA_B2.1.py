# Name: Jesse Fajardo
# Class: CS2300

import sympy as sp

#gets input for the flows from the user
flow1 = int(input('Enter flow1: '))
flow2 = int(input('Enter flow2: '))
flow3 = int(input('Enter flow3: '))
flow4 = int(input('Enter flow4: '))

#creates the mat with the flows
mat1 = sp.Matrix([[1,1,0,0,flow1],
                [1,0,0,1,flow2],
                [0,1,1,0,flow3],
                [0,0,1,1,flow4]])

print("The flow mat: ")
print(mat1)

#gets the reduced form
m_rref, pivots = mat1.rref()

print("The reduced mat: ")
#print(m_rref)
sp.pprint(m_rref)