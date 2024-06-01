n = int(input())

even, odd, positive, negative = [], [], [], []
lists = {"even": even, "odd": odd, "positive": positive, "negative": negative}

for _ in range(n):
    number = int(input())
    positive.append(number) if number >= 0 else negative.append(number)
    even.append(number) if number % 2 == 0 else odd.append(number)

print(lists.get(input()))
