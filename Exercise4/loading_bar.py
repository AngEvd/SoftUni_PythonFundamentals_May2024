def main():
    loading_bar(int(input()))


def loading_bar(n):
    if n == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        percent_count = n // 10
        dots_count = 10 - percent_count
        print(f"{n}% ", end="")
        print(f"[{'%' * percent_count}{'.' * dots_count}]")
        print("Still loading...")


if __name__ == '__main__':
    main()
