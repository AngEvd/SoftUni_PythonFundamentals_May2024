legendary_materials = {"shards": 0, "fragments": 0, "motes": 0}
legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
junk = {}
obtained = False

while not obtained:
    line = input().lower().split()

    for i in range(0, len(line), 2):
        quantity = int(line[i])
        material = line[i + 1]
        if material in legendary_materials:
            legendary_materials[material] += quantity
            if legendary_materials[material] >= 250:
                print(f"{legendary_items[material]} obtained!")
                legendary_materials[material] -= 250
                obtained = True
                break
        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += quantity

for material, quantity in legendary_materials.items():
    print(f"{material}: {legendary_materials[material]}")

for material, quantity in junk.items():
    print(f"{material}: {junk[material]}")
