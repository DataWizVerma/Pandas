import pandas as pd

# Data
data = {
    'Id': ["S01", "S02", "S03", "S04", "S05"],
    'Student': ["Amit", "John", "Jacob", "David", "Steve"],
    'Rank': [1, 2, 3, 5, 2],
    'Marks': [95, 70, 80, 60, 90]
}

# Create DataFrame
dataFrame = pd.DataFrame(data)

# Print the original DataFrame
print("Student Record:\n", dataFrame)

# Add a new column 'Roll no' using assign()
res = dataFrame.assign(Roll_no=[101, 102, 103, 104, 105])

# Print the updated DataFrame
print("\nUpdated DataFrame:\n", res)
