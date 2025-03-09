import json

with open("pt.json", 'w') as f:
    json.dump(("ch/", "tr/"), f)