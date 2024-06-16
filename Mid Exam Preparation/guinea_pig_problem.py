def main():
    food, hay, cover, pet_weight = float(input()), float(input()), float(input()), float(input())

    for day in range (1, 31):
        food -= 0.3
        if day % 2 == 0:
            hay -= 0.05 * food
        if day % 3 == 0:
            cover -= pet_weight / 3
        if any([food <= 0, hay <= 0, cover <= 0]):
            print("Merry must go to the pet store!")
            exit()

    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")


if __name__ == '__main__':
    main()
