""" Comparison of main functions for Time Complexity (using Plotly Express).

    Plotly simple line plot: https://plot.ly/python/line-charts/#simple-line-plot
"""
import plotly.graph_objects as go
import numpy as np
import math

np.random.seed(1)

n = np.arange(1, 6, 1) # (start, stop, step)

# Logarithmic function
log_f = [np.log(i) for i in n]

# n log n
n_log = [i * np.log(i) for i in n]

# Quadratic function
quad = n**2 

# Cubic function
cub = n**3

# Exponential function
exp = 2**n

# Factorial function
fact = [math.factorial(i) for i in n]

# Create traces
fig = go.Figure()
fig.add_trace(go.Scatter(x=n, y=log_f, mode='lines', name='$\log n$'))
fig.add_trace(go.Scatter(x=n, y=n, mode='lines', name='$n$'))
fig.add_trace(go.Scatter(x=n, y=n_log, mode='lines', name='$n \cdot \log n$'))
fig.add_trace(go.Scatter(x=n, y=quad, mode='lines', name='$n^2$'))
fig.add_trace(go.Scatter(x=n, y=cub, mode='lines', name='$n^3$'))
fig.add_trace(go.Scatter(x=n, y=exp, mode='lines', name='$2^n$'))
fig.add_trace(go.Scatter(x=n, y=fact, mode='lines', name='$n!$'))

# Add plot and axes titles
fig.update_layout(title='Time Complexity', xaxis_title='$n$', yaxis_title='$T(n)$')

fig.show()
