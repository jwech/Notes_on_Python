import pygal
from die import Die

die1 = Die()
die2 = Die()

results = [die1.roll_die() * die2.roll_die() for i in range(5000)]
values = list(set([x*y for x in range(1, die1.num_sides+1) for y in range(1, die2.num_sides+1)]))
values.sort()
# print(values)
frequencies = [results.count(value) for value in values]

bar = pygal.Bar()

bar.title = 'Results of rolling two D6 50000 times'
bar.x_labels = [str(i) for i in values]
bar.x_title = 'Results'
bar.y_title = 'Frequencies of Result'

bar.add('D6 * D6', frequencies)

bar.render_to_file('die_visual.svg')