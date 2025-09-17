import numpy as np
import matplotlib.pyplot as plt
from scipy import stats, optimize, signal

print("============================")
print("   Welcome to SciPy Demo    ")
print("============================")

# ---------------------------------------------------------------
# 1. What is SciPy?
# ---------------------------------------------------------------
print("\n[INFO] SciPy is a scientific computation library built on top of NumPy.")
print("It provides many optimized functions for statistics, optimization, and signal processing.")

# ---------------------------------------------------------------
# 2. SciPy uses NumPy underneath
# ---------------------------------------------------------------
print("\n[IMPORTANT NOTE] SciPy is built on NumPy, so NumPy arrays are used throughout.")

# Example: creating NumPy data
x = np.linspace(-5, 5, 100)
y = np.sin(x)

print("\nExample NumPy Array (first 5 values):", x[:5])

# ---------------------------------------------------------------
# 3. Statistics with SciPy (using scipy.stats)
# ---------------------------------------------------------------
print("\n============================")
print("   Statistics Example       ")
print("============================")

# Normal Distribution
mean, std_dev = 0, 1
normal_dist = stats.norm(loc=mean, scale=std_dev)

# Generate random samples
samples = normal_dist.rvs(size=1000)
print("Generated 1000 random samples from Normal Distribution (mean=0, std=1)")

# Plot Histogram of samples
plt.figure(figsize=(7, 4))
plt.hist(samples, bins=30, density=True, alpha=0.6, color='g', label='Sampled Data')
plt.plot(x, normal_dist.pdf(x), 'r-', lw=2, label='PDF (Theoretical)')
plt.title("Normal Distribution using SciPy Stats")
plt.legend()
plt.show()

# ---------------------------------------------------------------
# 4. Optimization Example (using scipy.optimize)
# ---------------------------------------------------------------
print("\n============================")
print("   Optimization Example     ")
print("============================")

# Function to minimize: f(x) = x^2 + 10*sin(x)
def func(x):
    return x**2 + 10 * np.sin(x)

# Use minimize from scipy.optimize
result = optimize.minimize(func, x0=2)  # starting point x0=2

print("Function: f(x) = x^2 + 10*sin(x)")
print("Optimization Result:")
print(result)
print("\n[IMPORTANT NOTE] Optimization helps in finding minima/maxima of functions.")

# Visualize function and minimum
x_vals = np.linspace(-10, 10, 400)
y_vals = func(x_vals)
plt.figure(figsize=(7, 4))
plt.plot(x_vals, y_vals, label='f(x) = x^2 + 10*sin(x)')
plt.scatter(result.x, result.fun, color='red', s=80, label='Minimum Found')
plt.title("Function Optimization using SciPy")
plt.legend()
plt.show()

# ---------------------------------------------------------------
# 5. Signal Processing Example (using scipy.signal)
# ---------------------------------------------------------------
print("\n============================")
print("   Signal Processing Example")
print("============================")

# Create a noisy signal
t = np.linspace(0, 1, 500, endpoint=False)
sig = np.sin(2 * np.pi * 7 * t) + 0.5 * np.random.randn(500)

# Apply a low-pass filter
b, a = signal.butter(4, 0.1)  # 4th order Butterworth filter
filtered_signal = signal.filtfilt(b, a, sig)

print("Generated a noisy sine wave (7 Hz) and applied a low-pass filter.")

plt.figure(figsize=(7, 4))
plt.plot(t, sig, label='Noisy Signal')
plt.plot(t, filtered_signal, label='Filtered Signal', linewidth=2)
plt.title("Signal Processing with SciPy (Low-pass filter)")
plt.legend()
plt.show()

# ---------------------------------------------------------------
# 6. SciPy Codebase
# ---------------------------------------------------------------
print("\n[INFO] SciPy is open source. Its source code is available here:")
print("GitHub Repository: https://github.com/scipy/scipy")

print("\n============================")
print("   End of SciPy Demonstration")
print("============================")
