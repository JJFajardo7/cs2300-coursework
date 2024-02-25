# Name: Jesse Fajardo
# Class: CS2300

import numpy as np

codingMat = np.mat([[1,-1,-1,1], 
                [2, -3, -5, 4],
                [-2, -1, -2, 2],
                [3, -3, -1, 2]])

inverseCodingMat = np.linalg.inv(codingMat)

#imports the encrypted message
file1Name = input("Enter file 1 name: ")
inputMessage = np.loadtxt(file1Name).astype(int)
colSize2 = inputMessage.size

#used to set num collumns of the encrypted message mat
messageSize = int(colSize2/4)
if(len(inputMessage)%4 != 0):
    messageSize += 1

#reshapes the message into a matrix
encryptedMat = inputMessage.reshape(4, messageSize).astype(int)

#deciphers the matrix
mat4 = (inverseCodingMat @ encryptedMat).round().astype(int)

#gets the size of the mat
rowSize4, colSize4 = mat4.shape

decryptedMessage = ""

#translate the decrypted message from unicode to a chars
for i in range(colSize4):
        for j in range(rowSize4):
            decryptedMessage += (chr(np.array(mat4)[j][i]))

print("The decrypted message: ")
print(decryptedMessage)

#removes any nulls
if '\x00' in decryptedMessage:
    decryptedMessage=' '.join(decryptedMessage.split('\x00'))

#puts decrypted message into a file
decryptedMatFileName = input("Enter name for new file with the encrypted message: ")
with open(decryptedMatFileName, 'w') as decryptedMatFile:
        decryptedMatFile.write(decryptedMessage)
