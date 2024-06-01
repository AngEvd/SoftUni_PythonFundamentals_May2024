n = int(input())

open_bracket_expected = False
for i in range(n):
    line = input()
    if line == "(":
        if open_bracket_expected:
            exit(print("UNBALANCED"))
        open_bracket_expected = True
    elif line == ")":
        if not open_bracket_expected:
            exit(print("UNBALANCED"))
        open_bracket_expected = False


print("UNBALANCED") if open_bracket_expected else print("BALANCED")
