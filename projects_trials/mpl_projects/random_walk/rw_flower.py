import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

plt.figure(figsize=(12, 6))
plt.plot(rw.x_values, rw.y_values, linewidth=1)


plt.show()