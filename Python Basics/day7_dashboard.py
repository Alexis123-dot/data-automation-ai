import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data with predictions
data = pd.read_csv("clean_students.csv")

# Create a new column PASS=1 / FAIL=0 for plotting
data["pass_numeric"] = data["status"].apply(lambda x: 1 if x=="PASS" else 0)

# Summary statistics
print("\nSUMMARY STATISTICS")
print(data.describe())

# Average by gender
avg_gender = data.groupby("gender")[["math_score","reading_score","writing_score","pass_numeric"]].mean()
print("\nAVERAGE SCORES BY GENDER")
print(avg_gender)

# Simple Dashboard: Pass vs Fail count
status_counts = data["status"].value_counts()
plt.figure(figsize=(6,4))
status_counts.plot(kind="bar", color=["green","red"])
plt.title("Pass vs Fail")
plt.ylabel("Number of Students")
plt.xlabel("Status")
plt.xticks(rotation=0)
plt.savefig("pass_fail_chart.png")
plt.show()

# Export final dataset
data.to_csv("final_students_report.csv", index=False)
print("\nSaved final_students_report.csv and pass_fail_chart.png")
