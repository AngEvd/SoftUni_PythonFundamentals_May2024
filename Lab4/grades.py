def main():
    print(grade(float(input())))


def grade(score):
    if 2 <= score <= 2.99:
        return "Fail"
    elif 3 <= score <= 3.49:
        return "Poor"
    elif 3.50 <= score <= 4.49:
        return "Good"
    elif 4.50 <= score <= 5.49:
        return "Very Good"
    else:
        return "Excellent"


if __name__ == "__main__":
    main()
