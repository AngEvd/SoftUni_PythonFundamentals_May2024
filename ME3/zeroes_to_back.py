input_list = input().split(", ")
integer_list = [int(value) for value in input_list]

zeroes = integer_list.count(0)

for _ in range(zeroes):
    integer_list.remove(0)
    integer_list.append(0)

print(integer_list)
