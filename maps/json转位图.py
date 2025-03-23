import json

with open("maps/test.json", "r") as f:
    pixels = json.load(f)

for row in pixels:
    print(row)