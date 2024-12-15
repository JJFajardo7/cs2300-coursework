import numpy as np
import matplotlib.pyplot as plt

filename = input("Enter file name: ")

#Read x, y from file
data = []
with open(filename, 'r') as file:
    for line in file:
        x, y = map(float, line.strip().split(','))
        data.append((x, y))

#Gets least squares regression line y = mx + b
x_vals = np.array([point[0] for point in data])
y_vals = np.array([point[1] for point in data])

#Gets slope and intercept
n = len(x_vals)
xSum = np.sum(x_vals)
ySum = np.sum(y_vals)
xySum = np.sum(x_vals * y_vals)
XSqrSum = np.sum(x_vals ** 2)

m = (n * xySum - xSum * ySum) / (n * XSqrSum - xSum ** 2)
b = (ySum - m * xSum) / n

print(f"The regression line is: y = {m}x + {b}")

#Plots the points and regression line
x_vals = np.array([point[0] for point in data])
y_vals = np.array([point[1] for point in data])

x_range = np.linspace(min(x_vals), max(x_vals), 100)
y_range = m * x_range + b

plt.scatter(x_vals, y_vals, color='blue')
plt.plot(x_range, y_range, color='red', label=f'Regression Line: y = {m}x + {b}')
plt.title('Least Squares Regression Line')
plt.xlabel('Price (x)')
plt.ylabel('Monthly Sales (y)')
plt.legend()
plt.grid(True)
plt.show()
