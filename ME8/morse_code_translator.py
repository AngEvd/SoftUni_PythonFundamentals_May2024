words = input().split("|")

morse_code = {
    ".-" : "A",
    "-..." : "B",
    "-.-." : "C",
    "-.." : "D",
    "." : "E",
    "..-." : "F",
    "--." : "G",
    "...." : "H",
    ".." : "I",
    ".---" : "J",
    "-.-" : "K",
    ".-.." : "L",
    "--" : "M",
    "-." : "N",
    "---" : "O",
    ".--." : "P",
    "--.-" : "Q",
    ".-." : "R",
    "..." : "S",
    "-" : "T",
    "..-" : "U",
    "...-" : "V",
    ".--" : "W",
    "-..-" : "X",
    "-.--" : "Y",
    "--.." : "Z",
}

decrypted_message = ""

for word in words:
    decrypted_message += " "
    chars = word.split()
    for char in chars:
        decrypted_message += morse_code[char]

print(decrypted_message)
