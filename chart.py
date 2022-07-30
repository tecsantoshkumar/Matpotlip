import matplotlib.pyplot as plt
   
Country = ['USA','Canada','Germany','UK','France']
GDP_Per_Capita = [45000,42000,52000,49000,47000]

plt.bar(Country, GDP_Per_Capita)
plt.title('Country Vs GDP Per Capita')
plt.xlabel('Country')
plt.ylabel('GDP Per Capita')
plt.show()

# importing matplotlib module
from matplotlib import pyplot as plt

# x-axis values
x = [5, 2, 9, 4, 7]

# Y-axis values
y = [10, 5, 8, 4, 2]

# Function to plot
plt.bar(x, y)

# function to show the plot
plt.show()
