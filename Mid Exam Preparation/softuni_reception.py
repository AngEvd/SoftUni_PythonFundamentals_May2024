def main():
    capacity1, capacity2, capacity3 = int(input()), int(input()), int(input())
    students = int(input())

    time_needed = 0

    while True:
        if students <= 0:
            break
        else:
            time_needed += 1
            if time_needed % 4 != 0:
                students -= capacity1 + capacity2 + capacity3

    print(f"Time needed: {time_needed}h.")


if __name__ == '__main__':
    main()
