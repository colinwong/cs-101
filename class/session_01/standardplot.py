# https://code.visualstudio.com/docs/python/python-tutorial

import matplotlib.pyplot as plt
import numpy as np

# Note:
# matplotlib cannot show graphs Windows/WSL as it lacks the necessary
# UI support.

# Create a list of evenly-spaced numbers over the range
x = np.linspace(0, 20, 100)

# Plot the sine of each x point
plt.plot(x, np.sin(x))

# Display the plot
plt.show()
