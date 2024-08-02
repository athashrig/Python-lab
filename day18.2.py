import numpy as np

# Employee data for full-time employees
full_time_employees = np.array([
    [101, 'John Doe', 'Full-Time', 55000],
    [102, 'Jane Smith', 'Full-Time', 60000],
    [103, 'Mike Johnson', 'Full-Time', 52000]
])

# Employee data for part-time employees
part_time_employees = np.array([
    [201, 'Alice Brown', 'Part-Time', 25000],
    [202, 'Bob Wilson', 'Part-Time', 28000],
    [203, 'Emily Davis', 'Part-Time', 22000]
])

# Combine the full-time and part-time employee data
all_employees = np.concatenate((full_time_employees, part_time_employees), axis=0)

# Print the combined employee data
print("Combined Employee Data:")
print(all_employees)

# Define column names for the combined data
column_names = ['Employee ID', 'Name', 'Type', 'Salary']

# Print the combined data with column names
print("\nCombined Employee Data with Column Names:")
print(column_names)
for employee in all_employees:
    print(employee)
