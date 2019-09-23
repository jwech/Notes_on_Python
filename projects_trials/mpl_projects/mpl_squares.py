import matplotlib.pyplot as plt


'''plt.plot() to match the output values'''
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.plot(input_values, squares, linewidth=5) # linewidth: the thick of the line

plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of value', fontsize=14)

# Set the size of scale
plt.tick_params(axis='both', labelsize=10)

plt.show()

