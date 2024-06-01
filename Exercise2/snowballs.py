snowballs_count = int(input())

snowballs = []

for i in range(1, snowballs_count + 1):
    weight, time, quality = int(input()), int(input()), int(input())
    value = round((weight / time) ** quality)
    snowball = {
        "weight": weight,
        "time": time,
        "quality": quality,
        "value": value
    }
    snowballs.append(snowball)

snowballs.sort(reverse=True, key=lambda x: x["value"])

print(f"{snowballs[0]['weight']} : {snowballs[0]['time']} = {snowballs[0]['value']} ({snowballs[0]['quality']})")
