import json

ch = input("选择资源包_")
tr = input("选择地图_")

with open("pt.json", 'w') as f:
    json.dump((ch, tr), f)