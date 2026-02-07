name = "Alexander"
age = 28
goal = "Data & Automation Engineer"

print(name)
print(age)
print(goal)

scores = [65, 72, 80, 90, 55]

print("Scores:", scores)
print("First score:", scores[0])
print("Last score:", scores[-1])

for s in scores:
    if s >= 75:
        print(s, "is a pass")
    else:
        print(s, "needs improvement")

student = {
    "name": "John",
    "math": 78,
    "english": 69,
    "science": 85
}

print("Math score:", student["math"])

def average(marks):
    return sum(marks) / len(marks)

print("Class average:", average(scores))
