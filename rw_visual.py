import matplotlib.pyplot as plt

from random_walk import RandomWalk

#makes a random walk, and plot the points

#keep making new walks as long as program is active
while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("make another walk? (y/n): ")
    if keep_running == 'n':
        break
    

