n = int(input())

for i in range(n):
    for j in range(n):
        for k in range(n):
            print(f"{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}")

# import itertools
# from string import ascii_lowercase
#
# n = int(input())
#
# for triple in itertools.product(ascii_lowercase[:n], repeat=3):
#     print("".join(triple))
