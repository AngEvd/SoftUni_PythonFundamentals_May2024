grades = {}
students_count = int(input())


for i in range(students_count):
    name = input()
    grade = float(input())
    if name not in grades:
        grades[name] = []
    grades[name].append(grade)

for name in grades:
    avg_grade = sum(grades[name]) / len(grades[name])
    if avg_grade >= 4.50:
        print(f"{name} -> {avg_grade:.2f}")
