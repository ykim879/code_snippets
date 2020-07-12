
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []


index = count()

# def animate(i):
#     x_vals.append(next(index))
#     y_vals.append(random.randint(0, 5))

#     plt.cla()
#     plt.plot(x_vals, y_vals, colors = )

def animate(i):
	data = pd.read_csv('data.csv')
	x = data['x_value']
	y1 = data['total_1']
	y2 = data['total_2']
	median1 = y1.median()
	median2 = y2.median()

	plt.cla()
	plt.plot(x, y1, label = "Channel 1")
	plt.plot(x, y2, label = "Channel 2")
	plt.axhline(median1, color = "#000000", label = "Channel 1 median")
	plt.axhline(median2, color = "#111111", label = "Channel 2 median")
	plt.legend(loc = "upper right") #location for constant location

	plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval = 1000)

plt.show()


