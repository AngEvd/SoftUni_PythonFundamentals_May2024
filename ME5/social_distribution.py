def main():
    population = [int(num) for num in input().split(", ")]
    min_wealth = int(input())

    for index, man in enumerate(population):
        wealthiest = max(population)
        wealthiest_index = population.index(wealthiest)
        if man < min_wealth:
            population[index] = min_wealth
            population[wealthiest_index] -= min_wealth - man
            if population[wealthiest_index] < min_wealth:
                print("No equal distribution possible")
                exit()

    print(population)


if __name__ == '__main__':
    main()
