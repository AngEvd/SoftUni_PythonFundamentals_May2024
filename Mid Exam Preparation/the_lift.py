def main():
    people_waiting = int(input())
    lift = list(map(int, input().split()))
    wagon_capacity = 4

    while True:
        if people_waiting == 0 and (sum(lift) / len(lift)) == wagon_capacity:
            break
        elif people_waiting == 0:
            print(f"The lift has empty spots!")
            break
        elif (sum(lift) / len(lift)) == wagon_capacity:
            print(f"There isn't enough space! {people_waiting} people in a queue!")
            break
        else:
            for i in range(len(lift)):
                if lift[i] < wagon_capacity:
                    people_boarding = min(people_waiting, wagon_capacity - lift[i])
                    lift[i] += people_boarding
                    people_waiting -= people_boarding

    print(" ".join(map(str, lift)))


if __name__ == '__main__':
    main()
