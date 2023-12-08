# Seminar X - Homework - Source Code
# Solution by Hus Lucian-Antonio, Group 914, IE

# Imports Section
import numpy as np
import matplotlib.pyplot as plt


# Define the given function and its gradient
def f(x, y, b):
    return (1/2)*(x**2 + b * y**2)


def gradient_f(x, y, b):
    return np.array([x, b * y])


# Define the optimal step-size using exact line search ( from point 'a' in homework )
def exact_line_search(x, y, b):
    return (x ** 2 + b * y ** 2)/(x ** 2 + (b ** 2) * (y ** 2))


# Gradient Descent function
def gradient_descent(b, iterations):
    # Initial point - Change to anything
    x, y = -20, 19

    # Store the points for plotting
    points = [(x, y)]

    for i in range(iterations):
        grad = gradient_f(x, y, b)
        learning_rate = exact_line_search(grad[0], grad[1], b)
        x -= learning_rate * grad[0]
        y -= learning_rate * grad[1]
        points.append((x, y))

    return np.array(points)


# Define contour plotting function
def plot_contour(b):
    x = np.linspace(-25, 25, 100)
    y = np.linspace(-25, 25, 100)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y, b)

    plt.contour(X, Y, Z, levels=50)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Contour Plot for b = {b}')


# Function to start the gradient descent and plot for different b values
def start():
    # Parameters
    b_values = [1/2, 1/5, 1/10]
    iterations = 50

    """
    As 'b' gets smaller we notice the enlargement of the level set ellipse on the y-axis
    Also as 'b' gets smaller the number of steps to converge does not increase or decrease significantly
    Gradient Descent for this function is somewhat like a ln function ??
    """

    # Plotting for each b value
    for b in b_values:
        plt.figure()
        plot_contour(b)
        points = gradient_descent(b, iterations)
        plt.plot(points[:, 0], points[:, 1], marker='o', linestyle='-', color='blue')
        plt.scatter(points[-1, 0], points[-1, 1], color='green', label='Minimum')
        plt.legend()
        plt.tight_layout()

    plt.show()


# Start the visualization
start()
