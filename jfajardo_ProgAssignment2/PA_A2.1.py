# Name: Jesse Fajardo
# Class: CS2300

import numpy as np

#coding matrix
codingMat = np.mat([[1,-1,-1,1], 
                [2, -3, -5, 4],
                [-2, -1, -2, 2],
                [3, -3, -1, 2]])

#gets the input
file1Name = input("Enter file 1 name: ")
inputMessage = open(file1Name, 'r').read()

#used to set num collumns in the unicode mat
messageSize = int(len(inputMessage)/4)
if(len(inputMessage)%4 != 0):
    messageSize += 1

unicodeMat = np.zeros((4, messageSize))
rowSize, colSize = unicodeMat.shape
inputMessageChars = list(inputMessage)
inputMessageNums = list()

#fills the matrix with 
tracker = 0
for i in range(colSize):
        for j in range(rowSize):
            if(tracker < len(inputMessage)):
                unicodeMat[j][i] = ord(inputMessageChars[tracker])
                tracker += 1

print("The unicode message in a matrix: ")
print(unicodeMat)

#create the cipher mat
cipherMat = codingMat @ unicodeMat

print("The encrypted mat: ")
print(cipherMat)

rowSize2, colSize2 = cipherMat.shape

#puts cipher into a list
encryptedMessage = cipherMat.reshape(1, rowSize2*colSize2)
inputMessageNums = encryptedMessage.tolist()

print("The encrypted message: ")
print(inputMessageNums)

#puts the list into a file
encryptedMatFileName = input("Enter name for new file with the encrypted message: ")
np.savetxt(encryptedMatFileName, inputMessageNums, fmt='%.2f')

