from math import floor

centuries = int(input())

years = 100 * centuries
days = floor(365.2422 * years)
hours = 24 * days
minutes = 60 * hours

print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
