# Name: Jesse Fajardo
# Class: CS2300

import sympy as sp

file1Name = input("Enter file 1 name: ")

#read file
with open(file1Name, 'r') as file:
    lines = file.readlines()

#D input
DInput = []
for line in lines[:3]:
    DInput.extend(map(float, line.split()))

#E input
EInput = []
for line in lines[3:]:
    EInput.extend(map(float, line.split()))

# create mats
D = sp.Matrix(3, 3, DInput)
E = sp.Matrix(3, 1, EInput)

# identity mat
I = sp.eye(3)

X = I - D

# if invertible
if X.det() == 0:
    print("Not invertible")
else:
    #inverse
    X = X.inv()
    roundedX = X.applyfunc(lambda x: round(x, 2))
    
    # Compute the output matrix X
    X = X * E
    roundedX = roundedX * E
    roundedX = roundedX.applyfunc(lambda x: round(x, 0))
    
    print("\nFully Rounded X:\n")
    sp.pprint(roundedX)
    
    #rounded only to tenths
    X = X.applyfunc(lambda x: round(x, 2))
    print("\nX:\n")
    sp.pprint(X)

