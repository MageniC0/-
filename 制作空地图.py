import json

tr_blank = [[[0 for x in range(4)] for y in range(4)] for z in range(4)]

with open("tr/blank.json", "w") as f:
    json.dump(tr_blank, f)