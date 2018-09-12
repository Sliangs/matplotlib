import matplotlib.pyplot as plt

from random_walk import RandomWalk

#makes a random walk, and plot the points

#keep making new walks as long as program is active
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    #set the size of the plotting window
    plt.figure(figsize=(10,6))
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("make another walk? (y/n): ")
    if keep_running == 'n':
        break
    
