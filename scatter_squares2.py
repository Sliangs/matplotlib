import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
    #to plot a series of points by making a list of x and y values
    
plt.scatter(x_values, y_values, c='red', edgecolor='none', s=20)
    #define colors (RBG model or name of color)
    #to remove outlines around point, pass edgecolor argument
    #plots a single point at those x,y values and s argument to size the dot

plt.title("Squared Numbers", fontsize=22)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
    #sets title and label axis

plt.tick_params(axis='both', which='major', labelsize=14)
    #default is 'major'; apply arguments to which ticks...could be major/minor/both

plt.axis([0, 1100, 0, 1100000])
    #setting the range for each axis


plt.show(
    #to save plots automatically use
    #plt.savefig('squares_plot.png', bbox_inches='tight')
    
