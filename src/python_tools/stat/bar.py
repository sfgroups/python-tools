import matplotlib.pyplot as plt

# Data
fruits = ['Apples', 'Bananas', 'Oranges', 'Grapes', 'Berries']
votes = [30, 25, 20, 15, 10]

# Plot
plt.bar(fruits, votes)
plt.xlabel('Fruits')
plt.ylabel('Number of Votes')
plt.title('Favorite Fruit Survey')
plt.show()
