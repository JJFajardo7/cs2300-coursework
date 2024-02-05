# Name: Jesse Fajardo
# Class: CS2300

import numpy as np

#imports the matrices
file1Name = input("Enter file 1 name: ")
mat1 = np.loadtxt(file1Name)
rowSize1, colSize1 = mat1.shape
print("\n", rowSize1)
print("\nMat1")
print(mat1)

file2Name = input("Enter file 2 name: ")
mat2 = np.loadtxt(file2Name)
rowSize2, colSize2 = mat2.shape
print("\n", rowSize2)
print("\nMat2")
print(mat2)

if rowSize1 != rowSize2 or colSize1 != colSize2:
    print("\n***The 2 matrices cannot be added since they are not the same size. Please restart the program.***")
    matAddedFileName = input("Enter name for new file with the matrices added: ")
    with open(matAddedFileName, 'w') as matAddedFile:
        matAddedFile.write("\n***The 2 matrices cannot be added since they are not the same size. Please restart the program.***")
else:
    #add, print, and write
    matAdded = mat1 + mat2
    print("\nMatAdded")
    print(matAdded)
    matAddedFileName = input("Enter name for new file with the matrices added: ")
    np.savetxt(matAddedFileName, matAdded, fmt='%.2f')

