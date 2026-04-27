import random
import matplotlib.pyplot as plt
import math

x = [0]
y = [0]

target_x = 10
target_y = 10

for _ in range(1000):
    step_size = 0.2

    dx_target = target_x - x[-1]
    dy_target = target_y - y[-1]
    distance = math.sqrt(dx_target**2 + dy_target**2)

    if distance != 0:
        dx_target /= distance
        dy_target /= distance

    dx_random = random.uniform(-1, 1)
    dy_random = random.uniform(-1, 1)

    bias_strength = 0.6
    dx = bias_strength * dx_target + (1 - bias_strength) * dx_random
    dy = bias_strength * dy_target + (1 - bias_strength) * dy_random

    norm = math.sqrt(dx**2 + dy**2)
    dx /= norm
    dy /= norm

    x.append(x[-1] + step_size * dx)
    y.append(y[-1] + step_size * dy)

# Plot the path line
plt.plot(x, y, alpha=0.5, label="Path")

# Plot points every 20 steps to show progression
step_indices = list(range(0, len(x), 20))
plt.scatter([x[i] for i in step_indices],
            [y[i] for i in step_indices],
            s=20)

# Mark start and food location
plt.scatter(x[0], y[0], marker='o', label="Start")
plt.scatter(target_x, target_y, marker='x', label="Nutrient")

plt.title("Biased Random Walk with Visible Steps")
plt.legend()
plt.show()