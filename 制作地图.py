import json, re
help = """[help]
load [path]: 编辑已有地图
new [path]: 新建地图
cube [n]: 指定要放置的方块
set [x] [y] [z]: 在(x, y, z)放置方块
done: 完成编辑
"""

block = []

def set(n, x, y, z):
    block[z][y][x] = n

def new_():
    return [[[0 for x in range(4)] for y in range(4)] for z in range(4)]

def load():
    with open(name, "r") as f:
        return json.load(f)

def save():
    with open(name, "w") as f:
        json.dump(block, f)

def done():
    pass

while True:
    ln = input("_")
    if ln == "":
        break
    elif me := re.match(r"load (\w+)", ln):
        load(me.group(1))
    elif me := re.match(r"new (\w+)", ln):
        new(me.group(1))
    elif me := re.match(r"set (\d+) (\d+) (\d+)", ln):
        set_(int(me.group(1)), int(me.group(2)), int(me.group(3)))
    elif me := re.match(r"cube (\d+)", ln):
        cube(int(group(1)), int(group(2)))
    elif ln == "done":
        done()
    else:
        print(help)