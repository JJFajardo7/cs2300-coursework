# Name: Jesse Fajardo
# Class: CS2300

import os

#reads the matrix
def readMatrix(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    matrix = []
    for line in lines:
        row = [float(x) for x in line.split()]
        matrix.append(row)
    return matrix

file1Name = input("Enter file 1 name: ")
mat1 = readMatrix(file1Name)

file2Name = input("Enter file 2 name: ")
mat2 = readMatrix(file2Name)

rowSize1 = len(mat1)
colSize1 = len(mat1[0])
print("\n", rowSize1)

#prints mat1
print("\nMat1")
for row in mat1:
    print(" ".join(map(str, row)))

rowSize2 = len(mat2)
colSize2 = len(mat2[0])
print("\n", rowSize2)

#prints mat2
print("\nMat2")
for row in mat2:
    print(" ".join(map(str, row)))

if rowSize1 != rowSize2 or colSize1 != colSize2:
    print("\n***The 2 matrices cannot be added since they are not the same size. Please restart the program.***")
    matAddedFileName = input("Enter name for new file with the matrices added: ")
    with open(matAddedFileName, 'w') as matAddedFile:
        matAddedFile.write("\n***The 2 matrices cannot be added since they are not the same size. Please restart the program.***")
else:
    #adds mat1 and mat2
    matAdded = [[mat1[i][j] + mat2[i][j] for j in range(colSize1)] for i in range(rowSize1)]

    #prints the added matrix
    print("\nMatAdded")
    for row in matAdded:
        print(" ".join(map(lambda x: f"{x:.2f}", row)))

    #writes the added matrix to a file
    matAddedFileName = input("Enter name for new file with the matrices added: ")
    with open(matAddedFileName, 'w') as file:
        for row in matAdded:
            file.write(" ".join(map(str, row)) + "\n")

