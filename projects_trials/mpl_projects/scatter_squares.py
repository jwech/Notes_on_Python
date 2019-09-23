import matplotlib.pyplot as plt

'''plt.scatter() to draw scatter drawing'''

x_values = list(range(1, 10001))
y_values = [x**2 for x in x_values]

# c: the color of the line, (0, 0, 0) [0, 1]
# edgecolor: the color of the edge of point
# s: the thick of the point
# colormap: c=values, cmap=plt.cm.COLOR
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolor='none', s=40)

# Set title and label name
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of mark
plt.tick_params(axis='both', which='major', labelsize=10)

# Set range of each axis
plt.axis([0, 1100, 0, 1100000])

# plt.show()
plt.savefig('squares_plt.png', bbox_inches='tight')