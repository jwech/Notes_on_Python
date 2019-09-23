from random_walk import RandomWalk
import matplotlib.pyplot as plt

rw = RandomWalk()
rw.fill_walk()
point_numbers = list(range(rw.num_points))

plt.figure(figsize=(12, 6.5))

plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=1)
# Re-draw start and finish point
plt.scatter(0, 0, c='green', edgecolor='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

# Hide axis
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()

    # keep_running = input('Continue? ')
    # if keep_running == 'n':
    #     break

    