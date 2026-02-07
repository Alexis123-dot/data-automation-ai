import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load cleaned data
data = pd.read_csv("clean_students.csv")

# Features: math, reading, writing
X = data[["math_score", "reading_score", "writing_score"]]

# Target: status (PASS=1, FAIL=0)
y = data["status"].apply(lambda x: 1 if x=="PASS" else 0)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, y_pred)
print(f"Prediction Accuracy: {acc*100:.2f}%")

# Test on new student
new_student = [[70, 75, 80]]  # math, reading, writing
prediction = model.predict(new_student)
status = "PASS" if prediction[0]==1 else "FAIL"
print(f"New student prediction: {status}")
