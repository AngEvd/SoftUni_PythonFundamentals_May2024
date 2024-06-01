n = int(input())

positive, negative = [], []

for _ in range(n):
    number = int(input())
    positive.append(number) if number >= 0 else negative.append(number)

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(negative)}")
