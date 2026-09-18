#!/usr/bin/env python3
"""Stacked bar graph of the number of fruit each person possesses."""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

people = ['Farrah', 'Fred', 'Felicia']
names = ['apples', 'bananas', 'oranges', 'peaches']
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']

bottom = np.zeros(fruit.shape[1])
for row, name, color in zip(fruit, names, colors):
    plt.bar(people, row, width=0.5, bottom=bottom, color=color, label=name)
    bottom += row

plt.ylabel('Quantity of Fruit')
plt.ylim(0, 80)
plt.yticks(np.arange(0, 81, 10))
plt.title('Number of Fruit per Person')
plt.legend()
plt.show()
