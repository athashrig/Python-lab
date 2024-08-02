# 1. Calculate the total revenue generated by two product categories in a store

import numpy as np

# Revenue data for two product categories
category1_revenue = np.array([500, 600, 700, 550])
category2_revenue = np.array([450, 700, 800, 600])

# Calculate the total revenue by adding the respective elements of the two arrays
total_revenue = category1_revenue + category2_revenue

# Print the total revenue
print("Total Revenue:", total_revenue)

# Output:
# Total Revenue: [ 950 1300 1500 1150]