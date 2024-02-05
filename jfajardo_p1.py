# Name: Jesse Fajardo
# Class: CS2300

print("Mat1")
print("Jesse = 5")
print("Fajardo = 7", )
mat1 = [[0 for _ in range(5)] for _ in range(7)]
k = 1

#sets mat1 nums
for i in range(7):
    for j in range(5):
        mat1[i][j] = k
        k += 1

#prints mat1
for i in range(7):
    print()
    for j in range(5):
        print(f"{mat1[i][j]} ", end="")


print("\n\nMat2")
print("Jesse = 5")
print("Fajardo = 7", )
mat2 = [[0 for _ in range(5)] for _ in range(7)]
k = 2

#sets mat2 nums
for i in range(5):
    for j in range(7):
        mat2[j][i] = k
        k += 3

#prints mat2
for i in range(7):
    print()
    for j in range(5):
        print(f"{mat2[i][j]} ", end="")


print("\n\nMat3")
mat3 = [[0 for _ in range(4)] for _ in range(2)]
k = 10

#sets mat3 nums
for i in range(2):
    for j in range(4):
        mat3[i][j] = k
        k -= 2

#prints mat3
for i in range(2):
    print()
    for j in range(4):
        print(f"{mat3[i][j]} ", end="")


print("\n\nMat4")
mat4 = [[0 for _ in range(2)] for _ in range(4)]
k = -6

#sets mat4 nums
for i in range(2):
    for j in range(4):
        mat4[j][i] = k
        k += 1.5

#prints mat4
for i in range(4):
    print()
    for j in range(2):
        print(f"{mat4[i][j]} ", end="")




#Mat1 File
with open("jfajardo_p1_mat1.txt", "w") as file:
    for i in range(7):
        for j in range(5):
            file.write(str(mat1[i][j]) + " ")
        file.write("\n")

#Mat2 File
with open("jfajardo_p1_mat2.txt", "w") as file:
    for i in range(7):
        for j in range(5):
            file.write(str(mat2[i][j]) + " ")
        file.write("\n")

#Mat3 File
with open("jfajardo_p1_mat3.txt", "w") as file:
    for i in range(2):
        for j in range(4):
            file.write(str(mat3[i][j]) + " ")
        file.write("\n")

#Mat4 File
with open("jfajardo_p1_mat4.txt", "w") as file:
    for i in range(4):
        for j in range(2):
            file.write(str(mat4[i][j]) + " ")
        file.write("\n")

