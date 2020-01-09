""" Comparison of main functions for Time Complexity (using Matplotlib).
"""
import matplotlib.pyplot as plt
import numpy as np
import math

# Constructing a graph for the less expensive functions
n = np.arange(1, 6, 1) # (start, stop, step)

# Logarithmic function
y = [np.log(i) for i in n]
plt.plot(n, y, label="$log(n)$")

# Linear function
y = n 
plt.plot(n, y, label="$n$")

# n log n
y = [i * np.log(i) for i in n]
plt.plot(n, y, label="$n \cdot \log(n)$")

# Quadratic function
y = n**2 
plt.plot(n, y, label="$n^2$")

# Cubic function
y = n**3
plt.plot(n, y, label="$n^3$")

# Exponential function
y = 2**n
plt.plot(n, y, label="$2^n$")

# Factorial function
y = [math.factorial(i) for i in n]
plt.plot(n, y, label="$n!$")

plt.legend()
plt.ylabel('$T(n)$')
plt.xlabel('$n$')
plt.title('Time Complexity')
plt.show()
