import pandas as pd

# Load the CSV file
data = pd.read_csv("students.csv")

# Show first 5 rows
print(data.head())

# Average math score
print("\nAverage math score:")
print(data["math score"].mean())

# Select students who passed (math score >= 75)
passed = data[data["math score"] >= 75]

print("\nStudents who passed math:")
print(passed)

# Save to new file
passed.to_csv("passed_students.csv", index=False)
print("\nSaved passed_students.csv successfully!")
