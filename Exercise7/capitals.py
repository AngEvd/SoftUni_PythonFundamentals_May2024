countries = input().split(", ")
capitals = input().split(", ")

country_capitals = {k: v for k, v in zip(countries, capitals)}

for country in country_capitals:
    print(f"{country} -> {country_capitals[country]}")
