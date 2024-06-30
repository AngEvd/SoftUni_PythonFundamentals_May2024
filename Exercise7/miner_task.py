input_lines = []
resources = {}

while True:
    resource = input()
    if resource == "stop":
        break
    else:
        quantity = int(input())
        if resource not in resources:
            resources[resource] = 0
        resources[resource] += quantity

for resource in resources:
    print(f"{resource} -> {resources[resource]}")
