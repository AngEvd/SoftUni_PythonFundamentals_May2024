courses = {}

while True:
    command_line = input()
    if command_line == "end":
        break
    else:
        course_name, student_name = command_line.split(" : ")
        if course_name not in courses:
            courses[course_name] = []
        courses[course_name].append(student_name)

for course_name, students in courses.items():
    print(f"{course_name}: {len(students)}")
    for student in students:
        print(f"-- {student}")
