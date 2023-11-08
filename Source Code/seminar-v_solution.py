"""
Homework for Seminar V - Exercise 8

Let f : R → R be differentiable. To minimize f, consider the gradient descent method: xn+1 = xn − ηf'(xn)
where x1 ∈ R and η > 0 (learning rate). Use Python (numerics or graphics) for the following

(a) Take a convex f and show that for small η the method converges to the minimum of f.
(b) Show that by increasing η the method can converge faster (in fewer steps).
(c) Show that taking η too large might lead to the divergence of the method.
(d) Take a non-convex f and show that the method can get stuck in a local minimum.
"""

""" Imports Section Below """
import matplotlib.pyplot


""" Convex Function Tests - f(x) = x^2, f'(x) = 2 * x - Below"""
def convex_function(x):
    return x**2

def gradient_of_convex_function(x):
    return 2 * x


# Gradient Descent function
def gradient_descent(x0, learning_rate, num_iterations):

    x = x0
    x_history = [x]

    # Formula from assignment
    for _ in range(num_iterations):
        x = x - learning_rate * gradient_of_convex_function(x)
        x_history.append(x)
    return x_history


# Visualizer of the Convex Function
def visualizer_convex_function(trajectory):

    # Main Graph
    matplotlib.pyplot.plot(range(len(trajectory)), [convex_function(x) for x in trajectory])

    # Labels and Print
    matplotlib.pyplot.xlabel('Iterations')
    matplotlib.pyplot.ylabel('f(x)')
    matplotlib.pyplot.show()


# Learning Rate Variation Tests
def small_learning_rate_test():

    # Testing Parameters
    x0 = 1
    learning_rate = 0.1
    num_iterations = 25

    # Run Gradient Descent
    trajectory = gradient_descent(x0, learning_rate, num_iterations)
    visualizer_convex_function(trajectory)


def increasing_learning_rate_tests():
    x0 = 1
    learning_rate = 0.25
    num_iterations = 25

    while learning_rate <= 10:

        # Visualizing for each new value of the learning rate
        trajectory = gradient_descent(x0, learning_rate, num_iterations)
        visualizer_convex_function(trajectory)

        # Doubling the learning rate at each step
        learning_rate *= 2


""" Non-Convex Function Tests - f(x) = x ^ 3, f'(x) = 3*(x^2) - Below """
def non_convex_function(x):
    return x**3

def gradient_of_non_convex_function(x):
    return 3 * (x ** 2)


def gradient_descent_non_convex_function(x0, learning_rate, num_iterations):

    x = x0
    x_history = [x]

    # Formula from assignment
    for _ in range(num_iterations):
        x = x - learning_rate * gradient_of_non_convex_function(x)
        x_history.append(x)
    return x_history


def visualizer_non_convex_function(trajectory):

    # Main Graph
    matplotlib.pyplot.plot(range(len(trajectory)), [non_convex_function(x) for x in trajectory])

    # Labels and Print
    matplotlib.pyplot.xlabel('Iterations')
    matplotlib.pyplot.ylabel('f(x)')
    matplotlib.pyplot.show()


# Learning Rate Variation Tests
def small_learning_rate_test_non_convex():

    # Testing Parameters
    x0 = 1
    learning_rate = 0.1
    num_iterations = 25

    # Run Gradient Descent
    trajectory = gradient_descent(x0, learning_rate, num_iterations)
    visualizer_non_convex_function(trajectory)


def increasing_learning_rate_tests_non_convex():
    x0 = 1
    learning_rate = 0.25
    num_iterations = 25

    while learning_rate <= 10:

        # Visualizing for each new value of the learning rate
        trajectory = gradient_descent(x0, learning_rate, num_iterations)
        visualizer_non_convex_function(trajectory)

        # Doubling the learning rate at each step
        learning_rate *= 2


""" Main Function """
def main():

    # Running the tests for the convex function
    small_learning_rate_test()
    increasing_learning_rate_tests()

    # Running the tests for the non-convex function
    small_learning_rate_test_non_convex()
    increasing_learning_rate_tests_non_convex()


main()
