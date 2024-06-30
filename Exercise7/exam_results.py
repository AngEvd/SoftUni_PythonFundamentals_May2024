results = {}
submissions = {}

while True:
    command_line = input()

    if command_line == "exam finished":
        break

    elif "banned" in command_line:
        username = command_line.strip("-banned")
        if username in results:
            del results[username]
    else:
        username, language, points = command_line.split("-")
        points = int(points)

        if username not in results:
            results[username] = {}

        if language not in results[username]:
            results[username][language] = points
        else:
            results[username][language] = max(points, results[username][language])

        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1

print("Results:")
for username, result in results.items():
    for language, points in result.items():
        print(f"{username} | {points}")
print("Submissions:")
for language in submissions:
    print(f"{language} - {submissions[language]}")
