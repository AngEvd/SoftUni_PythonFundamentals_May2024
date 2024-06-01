string_one = input()
string_two = input()

converted_string = string_one
printed = string_one

for i in range(len(string_one)):
    left_part = string_two[:i+1]
    right_part = string_one[i+1:]
    mutated_string = left_part + right_part
    if mutated_string != printed:
        print(mutated_string)
        printed = mutated_string
