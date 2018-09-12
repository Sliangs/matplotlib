import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)
        #linewidth controls thickness of the line plot() generates
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
        #Sets chart title and labels axes
plt.tick_params(axis='both', labelsize=14)
        #Set size of tick labels
plt.show()
