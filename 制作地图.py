import json, re
help = """[help]
set [x] [y] [z]: 在(x, y, z)放置方块
cube [n]: 指定要放置的方块
done: 完成编辑
"""

name = input("地图的文件名_")
block = []

def set(n, x, y, z):
    block[z][y][x] = n

def new():
    return [[[0 for x in range(4)] for y in range(4)] for z in range(4)]

def load():
    with open(name, "r") as f:
        return json.load(f)

def save():
    with open(name, "w") as f:
        json.dump(block, f)

while True:
    ln = input("_")
    if ln == "":
        break
    # elif ...
    else:
        print(help)