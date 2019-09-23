import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=10)

plt.title('Cubes Number', fontsize=24)
plt.xlabel('Values', fontsize=14)
plt.ylabel('Cubes', fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=10)
plt.axis([0, 5100, 0, 125100000000])

plt.show()
