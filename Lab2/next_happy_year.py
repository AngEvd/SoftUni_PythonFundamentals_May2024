year = int(input())

while True:
    year += 1
    if len(str(year)) == len(set(str(year))):
        exit(print(year))
