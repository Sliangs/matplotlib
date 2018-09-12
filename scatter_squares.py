import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
    #to plot a series of points by making a list of x and y values
    
plt.scatter(x_values, y_values, s=100)
    #plots a single point at those x,y values and s argument to size the dot

plt.title("Squared Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
    #sets title and label axis

plt.tick_params(axis='both', which='major', labelsize=14)
    #default is 'major'; apply arguments to which ticks...could be major/minor/both


plt.show()
