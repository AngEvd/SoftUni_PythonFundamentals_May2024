lines_number = int(input())

total_sum = 0

for _ in range(lines_number):
    total_sum += ord(input())

print(f"The sum equals: {total_sum}")
