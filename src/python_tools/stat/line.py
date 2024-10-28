import matplotlib.pyplot as plt

# Data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
temperature = [20, 22, 24, 19, 21]

# Plot
plt.plot(days, temperature, marker='o')
plt.xlabel('Days')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over a Week')
plt.show()
