import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("school.db")

# Load cleaned data
data = pd.read_csv("clean_students.csv")

# Save to SQL
data.to_sql("students", conn, if_exists="replace", index=False)

# Query database
query = """
SELECT gender, status, COUNT(*) as total
FROM students
GROUP BY gender, status
"""

result = pd.read_sql(query, conn)

print("\nSTUDENTS BY GENDER AND STATUS")
print(result)

conn.close()
