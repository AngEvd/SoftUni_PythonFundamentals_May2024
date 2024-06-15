def main():
    students_number, lectures_number, bonus = int(input()), int(input()), int(input())

    attendances = []
    max_bonus, max_attendances = 0, 0

    for _ in range(students_number):
        attendances.append(int(input()))

    if attendances and lectures_number > 0:
        max_attendances = max(attendances)
        max_bonus = round(max_attendances / lectures_number * (5 + bonus))

    print(f"Max Bonus: {max_bonus}.")
    print(f"The student has attended {max_attendances} lectures.")


if __name__ == '__main__':
    main()
