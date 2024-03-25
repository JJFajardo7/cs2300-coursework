# Name: Jesse Fajardo
# Class: CS2300

import numpy as np
import math
import turtle as t

matD = np.mat([[0, 6, 5, 1, 3],
            [0, 0, 3, 3, 9],
            [1, 1, 1, 1, 1]])

file1Name = input("Enter file 1 name: ")
inputMessage = np.loadtxt(file1Name).astype(float)
colSize2 = inputMessage.size

inputList = inputMessage.tolist()

print(inputList)

order = list(str(int(inputList[5])))
print(order)
#point = [inputList[0], inputList[1]]

#print(point)

matPointPos = np.mat([[1, 0, inputList[0]],
                    [0, 1, inputList[1]],
                    [0, 0, 1]])

matPointNeg = np.mat([[1, 0, -inputList[0]],
                    [0, 1, -inputList[1]],
                    [0, 0, 1]])

matRotation = np.mat([[math.cos(math.radians(inputList[2])), -math.sin(math.radians(inputList[2])), 0],
                    [math.sin(math.radians(inputList[2])), math.cos(math.radians(inputList[2])), 0],
                    [0, 0, 1]])

matShear = np.mat([[1, inputList[3], 0],
                    [0, 1, 0],
                    [0, 0, 1]])

matScale = np.mat([[inputList[4], 0, 0],
                    [0, inputList[4], 0],
                    [0, 0, 1]])

matX = matScale @ matShear @ matPointPos @ matRotation @ matPointNeg @ matD

matList = [matRotation, matShear, matScale]

matFinal = matD

i = int(order[0])
j = 0
while(i != 0 and j < 3):
    i = int(order[j])
    
    if(i == 1):
        matFinal = matPointPos @ matList[i-1] @ matPointNeg @ matFinal
    else:
        matFinal = matList[i-1] @ matFinal
    
    j += 1

#s = turtle.getscreen()
#t = turtle.Turtle()
wn = t.Screen()
wn.xscale = 10
wn.yscale = 10
#t.getscreen()
# t.goto(matD[0,0], matD[1,0])
# t.goto(matD[0,4], matD[1,4])
# t.goto(matD[0,1], matD[1,1])
# t.goto(matD[0,2], matD[1,2])
# t.goto(matD[0,3], matD[1,3])

# t.clear()
t.penup()
t.goto(matFinal[0,0], matFinal[1,0])
t.pendown()
t.goto(matFinal[0,4], matFinal[1,4])
t.goto(matFinal[0,1], matFinal[1,1])
t.goto(matFinal[0,2], matFinal[1,2])
t.goto(matFinal[0,3], matFinal[1,3])

t.mainloop()

print()
print(matX)
print()
print(matFinal)
