text = input()

text_to_repeat = ""
times_to_repeat = ""
result = ""

used_symbols = set()

for i in range(len(text)):
    if not text[i].isdigit():
        if times_to_repeat:
            result += text_to_repeat * int(times_to_repeat)
            times_to_repeat = ""
            text_to_repeat = ""

        text_to_repeat += text[i].upper()
        used_symbols.add(text[i].lower())

    elif text[i].isdigit():
        times_to_repeat += text[i]

if times_to_repeat:
    result += text_to_repeat * int(times_to_repeat)

print(f"Unique symbols used: {len(used_symbols)}")
print(result)
