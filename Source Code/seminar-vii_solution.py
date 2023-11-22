# Seminar VII - Homework - Hus Lucian-Antonio, 914, IE

# Imports Section
import math


# Function to approximate the integral of e^(-x^2)
def integrate_trapezoidal(f, a, n):
    delta_x = 2 * a / n
    integral = 0
    for i in range(n + 1):
        x = -a + i * delta_x
        if i == 0 or i == n:
            integral += f(x) / 2
        else:
            integral += f(x)
    integral *= delta_x
    return integral


# Define the function e^(-x^2)
def func(x):
    return math.exp(-x ** 2)


def main():

    # Values of 'a' to check
    a_values = [1, 2, 5, 10, 50, 100, 500, 1000]

    # Calculate the integral for different values of a
    for a in a_values:
        integral = integrate_trapezoidal(func, a, 10000)  # Using 10000 points for accuracy
        print("For a = ", a, ", Integral ≈ ", integral)

    print()
    print("For reference, √π ≈ ", math.sqrt(math.pi))


main()
