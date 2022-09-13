from matplotlib import pyplot as plt
import numpy as np

years = np.arange(1950, 2011, 10)
gdp = np.array([300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3])

# create a line chart, years on x-axis and gdp on y-axis
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

# add a title
plt.title("Nominal GDP")

# add a label to the y-axis
plt.ylabel("Billions of $")
plt.show()