# Seminar VIII Homework - by Hus Lucian-Antonio, Group 914, IE

# Imports Section
import numpy as np
import matplotlib.pyplot as plt


# Function to check if a point is inside the unit ball for a given p-norm
def inside_unit_ball(point, p):
    norm = np.linalg.norm(point, ord=p)
    return norm <= 1


# Function to plot points inside the unit ball for various p-values in separate plots
def plot_unit_ball(p_values, num_points):

    # Iterate through each p-value
    for p in p_values:

        # Generate random points in the range [-1, 1]
        points = np.random.uniform(low=-1, high=1, size=(num_points, 2))

        # Filter points that are inside the unit ball for the given p-norm
        inside_points = [point for point in points if inside_unit_ball(point, p)]
        inside_points = np.array(inside_points)

        # Create a new figure and plot the points inside the unit ball
        plt.figure(figsize=(10, 10))
        plt.scatter(inside_points[:, 0], inside_points[:, 1], s=5)
        plt.title(f"p = {p}")
        plt.xlim([-2, 2])
        plt.ylim([-2, 2])
        plt.gca().set_aspect('equal', adjustable='box')
        plt.tight_layout()
        plt.show()


# Example usage:
def main():
    p_values = [1.25, 1.5, 3, 8]
    num_points = 10000
    plot_unit_ball(p_values, num_points)


main()
