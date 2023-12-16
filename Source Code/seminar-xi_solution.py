# Seminar XI Homework
# Made by Hus Lucian-Antonio, Group 914, IE

# Imports Section
import numpy as np
import matplotlib.pyplot as plt


# Given quadratic function 1/2 * ( xT * A * x )
def f(x, A):
    return 0.5 * np.dot(np.dot(x.T, A), x)


# Plotting the surface, gradient and contour lines
def plot_surface_and_gradients(A, title):
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = np.zeros_like(x)

    for i in range(len(x)):
        for j in range(len(y)):
            z[i, j] = f(np.array([x[i, j], y[i, j]]), A)

    fig = plt.figure(figsize=(12, 8))

    # 3D Surface plot
    ax = fig.add_subplot(121, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis')
    ax.set_title(title)

    # Contour plot with three contour lines
    plt.subplot(222)
    plt.contour(x, y, z, levels=3, colors='black')
    plt.title('Contour Lines')

    # Gradients at three different points
    points = [(-3, -3), (0, 0), (3, 3)]
    for point in points:
        grad = np.dot(A, point)
        ax.quiver(point[0], point[1], f(np.array(point), A), grad[0], grad[1], 0, color='red')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('equal')
    plt.tight_layout()


# Main Function of the program
def main():
    A_min = np.array([[4, 0], [0, 5]])
    A_max = np.array([[-4, 0], [0, -5]])
    A_saddle = np.array([[4, 0], [0, -5]])

    plot_surface_and_gradients(A_min, 'Unique Minimum')
    plot_surface_and_gradients(A_max, 'Unique Maximum')
    plot_surface_and_gradients(A_saddle, 'Saddle Point')

    plt.show()


if __name__ == "__main__":
    main()
