numbers = [int(x) for x in input().split(" ")]
n = int(input())

result = ""

for _ in range(n):
    smallest = min(numbers)
    numbers.remove(smallest)

for number in numbers:
    result += f"{number}, "

print(result.strip(", "))
