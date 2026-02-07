import pandas as pd

# Load dataset
data = pd.read_csv("students.csv")

# Show original info
print("ORIGINAL DATA")
print(data.info())

# Clean column names (remove spaces)
data.columns = data.columns.str.strip().str.lower().str.replace(" ", "_")

# Fill missing scores with average
data["math_score"] = data["math_score"].fillna(data["math_score"].mean())
data["reading_score"] = data["reading_score"].fillna(data["reading_score"].mean())
data["writing_score"] = data["writing_score"].fillna(data["writing_score"].mean())

# Create new column: average score
data["average_score"] = (
    data["math_score"] + data["reading_score"] + data["writing_score"]
) / 3

# Label pass/fail
data["status"] = data["math_score"].apply(lambda x: "PASS" if x >= 75 else "FAIL")

# Save cleaned data
data.to_csv("clean_students.csv", index=False)

# Summary
print("\nCLEANED DATA PREVIEW")
print(data.head())

print("\nSTUDENTS PASSED:", (data["status"] == "PASS").sum())
print("STUDENTS FAILED:", (data["status"] == "FAIL").sum())

print("\nSaved file: clean_students.csv")
