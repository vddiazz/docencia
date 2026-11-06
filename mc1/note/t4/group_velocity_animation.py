import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the waves
frequency1 = 3.0  # Frequency of the first wave
frequency2 = 2.5  # Frequency of the second wave
frequency3 = 2.0  # Frequency of the second wave
amplitude1 = 1.5  # Amplitude of the first wave
amplitude2 = 1.5  # Amplitude of the second wave
amplitude3 = 1.5  # Amplitude of the second wave

# Time values
t = np.linspace(0, 4 * np.pi, 1000)

# Create the waves
wave1 = amplitude1 * np.sin(2 * np.pi * frequency1 * t)
wave2 = amplitude2 * np.sin(2 * np.pi * frequency2 * t)
wave3 = amplitude3 * np.sin(2 * np.pi * frequency3 * t)

# Function to update the plot in the animation
def update(frame):
    result_wave = wave1 * np.sin(2 * np.pi * frequency2 * t + frame)
    line.set_ydata(result_wave)
    return line,

# Create the initial plot
fig, ax = plt.subplots()
line, = ax.plot(t, wave1 + wave2 + wave3)

# Create and run the animation
animation = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 100), interval=50)
plt.show()
