import pygal
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()
# print(len(rw.x_values))
rw_chart = pygal.XY(stroke=False)
rw_chart.title = 'Random walk of (x, y)'
rw_chart.add('(x, y)', [(rw.x_values[i], rw.y_values[i]) for i in range(rw.num_points) ])

rw_chart.render_to_file('rw_walk.svg')