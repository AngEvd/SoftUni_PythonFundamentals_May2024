usernames = input().split(", ")

for username in usernames:
    valid = True

    for char in username:
        if not char.isalnum() and char not in "-_":
            valid = False
            break

        elif not (3 <= len(username) <= 16) or username != username.strip():
            valid = False

    if valid:
        print(username)
