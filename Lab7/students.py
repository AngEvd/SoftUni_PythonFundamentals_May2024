students_by_course = {}

while True:
    user_line = input()
    if ':' in user_line:
        name, student_id, course = user_line.split(':')

        if course not in students_by_course:
            students_by_course[course] = []

        students_by_course[course].append((name, student_id))

    else:
        target_course = user_line.replace("_", " ")
        break

if target_course in students_by_course:
    for name, student_id in students_by_course[target_course]:
        print(f"{name} - {student_id}")


