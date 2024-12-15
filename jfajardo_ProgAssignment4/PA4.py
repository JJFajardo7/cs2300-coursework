import numpy as np
import matplotlib.pyplot as plt

def read_data_from_file(filename):
    """Reads ordered pairs (x, y) from a text file."""
    data = []
    with open(filename, 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split(','))
            data.append((x, y))
    return data

def compute_least_squares(data):
    """Computes the least squares regression line y = mx + b."""
    x_vals = np.array([point[0] for point in data])
    y_vals = np.array([point[1] for point in data])

    # Compute slope (m) and intercept (b)
    n = len(x_vals)
    sum_x = np.sum(x_vals)
    sum_y = np.sum(y_vals)
    sum_xy = np.sum(x_vals * y_vals)
    sum_x_squared = np.sum(x_vals ** 2)

    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
    b = (sum_y - m * sum_x) / n

    return round(m, 1), round(b, 1)

def plot_data_and_regression_line(data, m, b):
    """Plots the data points and the regression line."""
    x_vals = np.array([point[0] for point in data])
    y_vals = np.array([point[1] for point in data])

    # Create a range of x values for the regression line
    x_range = np.linspace(min(x_vals), max(x_vals), 100)
    y_range = m * x_range + b

    plt.scatter(x_vals, y_vals, color='blue', label='Data Points')
    plt.plot(x_range, y_range, color='red', label=f'Regression Line: y = {m}x + {b}')

    plt.title('Least Squares Regression Line')
    plt.xlabel('Price (x)')
    plt.ylabel('Monthly Sales (y)')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    filename = input("Enter the name of the text file containing the data: ")
    try:
        data = read_data_from_file(filename)
        m, b = compute_least_squares(data)
        print(f"The regression line is: y = {m}x + {b}")
        plot_data_and_regression_line(data, m, b)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()