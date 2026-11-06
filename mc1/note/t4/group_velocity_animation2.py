import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to calculate the sum of two sine functions
def sum_of_sines(x, freq1, freq2, amp1, amp2, phase1, phase2):
    return amp1 * np.sin(2 * np.pi * freq1 * x + phase1) + amp2 * np.sin(2 * np.pi * freq2 * x + phase2)

# Function to update the plot in each animation frame
def update(frame):
    line_sum.set_ydata(sum_of_sines(x, freq1, freq2, amp1, amp2, phase1, phase2 + frame / 10.0))
    line_sine1.set_ydata(amp1 * np.sin(2 * np.pi * freq1 * x + phase1 + frame / 10.0))
    line_sine2.set_ydata(amp2 * np.sin(2 * np.pi * freq2 * x + phase2 + frame / 10.0))
    return line_sum, line_sine1, line_sine2

# Parameters for the sine functions
freq1 = 2.5
freq2 = 2.0
amp1 = 1.0
amp2 = 1.0
phase1 = 0.0
phase2 = 0.0

# Create the x values
x = np.linspace(0, 4 * np.pi, 1000)

# Create the figure and three subplots
fig, (ax_sine1, ax_sine2, ax_sum) = plt.subplots(3, 1, figsize=(8, 6))

# Plot the first sine function
line_sine1, = ax_sine1.plot(x, amp1 * np.sin(2 * np.pi * freq1 * x + phase1))
ax_sine1.set_title('Sine Function 1')

# Plot the second sine function
line_sine2, = ax_sine2.plot(x, amp2 * np.sin(2 * np.pi * freq2 * x + phase2))
ax_sine2.set_title('Sine Function 2')

# Plot the sum of sine functions
line_sum, = ax_sum.plot(x, sum_of_sines(x, freq1, freq2, amp1, amp2, phase1, phase2))
ax_sum.set_title('Sum of Sine Functions')

# Set common labels
fig.text(0.5, 0.04, 'X-axis', ha='center')
fig.text(0.04, 0.5, 'Y-axis', va='center', rotation='vertical')

# Set animation
ani = FuncAnimation(fig, update, frames=range(100), blit=True)

plt.show()

