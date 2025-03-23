import json

pixels = [[[0, 0, 0, 0] for i in range(49)] for j in range(49)]
with open("maps/test.json", "w") as f:
    json.dump(pixels, f)