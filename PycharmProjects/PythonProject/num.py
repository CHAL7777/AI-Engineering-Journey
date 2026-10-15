import numpy as np

# 1. Imagine these are 3 data inputs (e.g., sensor readings)
inputs = np.array([2.5, 3.0, 1.5])

# 2. These are the AI's "weights" (importance scores for each input)
weights = np.array([0.8, -0.5, 1.2])

# 3. This is the bias (a constant adjustment value)
bias = 2.0

# 4. The AI math: Multiply inputs by weights element-by-element, then add them up
# NumPy does this instantly using the dot product!
output = np.dot(inputs, weights) + bias

print("AI Layer Output:", output)
