import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Generate data: mean 77, standard deviation 5, and 100 students
mean = 77
std_dev = 5
data = np.random.normal(mean, std_dev, 100)

# Generate the bell curve
x = np.linspace(mean - 3*std_dev, mean + 3*std_dev, 100)
y = stats.norm.pdf(x, mean, std_dev)

# Plot the bell curve
plt.plot(x, y, label='Bell Curve')
plt.xlabel('Test Scores')
plt.ylabel('Probability Density')
plt.title('Normal Distribution of Test Scores')
plt.show()
