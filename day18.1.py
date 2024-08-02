import numpy as np

temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])

# Define the threshold temperatures
hot_threshold = 35
cold_threshold = 5

hot_days = np.where(temperatures > hot_threshold)[0]
cold_days = np.where(temperatures < cold_threshold)[0]

# Print the results
print("Hot days:")
print(hot_days)
print("Temperatures on hot days:")
print(temperatures[hot_days])
print("\nCold days:")
print(cold_days)
print("Temperatures on cold days:")
print(temperatures[cold_days])
