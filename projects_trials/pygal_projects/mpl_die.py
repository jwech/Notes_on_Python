import matplotlib.pyplot as plt
from die import Die

die1 = Die()
die2 = Die()

x_values = [i for i in range(2, die1.num_sides+die2.num_sides+1)]
results = [die1.roll_die() + die2.roll_die() for i in range(10000)]
y_values = [results.count(result) for result in x_values]

plt.title("Frequencies of rolling D6+D6 10000 times", fontsize=18)
plt.xlabel("Result", fontsize=14)
plt.ylabel('Frequency', fontsize=14)

plt.scatter(x_values, y_values, s=40)

plt.show()