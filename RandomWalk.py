import random
import matplotlib.pyplot as plt


def complex_random_walk(num_steps, step_size_range=(0.1, 1.0), angle_range=(0, 2 * 3.14159), noise_factor=0.1):
    x, y = 0, 0  # Initial position
    x_history, y_history = [x], [y]  # Lists to store the positions

    for _ in range(num_steps):
        # Introduce randomness to the step size within a range
        step_size = random.uniform(*step_size_range)
        # Introduce randomness to the direction of the step within a range
        angle = random.uniform(*angle_range)

        # Calculate the new position with added noise
        x += step_size * (2 * random.random() - 1) + random.uniform(-noise_factor, noise_factor)
        y += step_size * (2 * random.random() - 1) + random.uniform(-noise_factor, noise_factor)

        # Append the new position to the history
        x_history.append(x)
        y_history.append(y)

    return x_history, y_history


if __name__ == "__main__":
    num_steps = 1000  # Number of steps in each random walk
    num_walks = 10  # Number of random walks to generate

    for i in range(num_walks):
        # Generate a complex random walk with added complexity
        x_hist, y_hist = complex_random_walk(num_steps, step_size_range=(0.1, 0.5), angle_range=(0, 2 * 3.14159),
                                             noise_factor=0.2)

        # Plot the complex random walk
        plt.figure(figsize=(8, 6))
        plt.plot(x_hist, y_hist, marker='o', markersize=2, linestyle='-', color='b')
        plt.title(f"Complex Random Walk {i + 1}")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)

        # Save the plot as a .png file
        plt.savefig(f"random_walk_{i + 1}.png")

        # Close the current plot to avoid overlapping plots
        plt.close()

    print("Random walk images saved successfully.")
