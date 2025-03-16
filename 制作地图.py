import json
import re

help = """[help]
load [name]: 编辑已有地图
new [name]: 新建地图
cube [n]: 指定要放置的方块
put [x] [y] [z]: 在指定位置放置方块
done: 完成编辑
output [name]: 另存文件
"""

class Block:
    def __init__():
        self.block = []
        self.name = ""
    
    def load():
        with open(self.name, "r") as f:
            self.block = json.load(f)
    
    def new():
        self.block = [[[0 for x in range(4)] for y in range(4)] for z in range(4)]
    
    def set_name(name):
        self.name = name
    










while True:
    ln = input("_")
    if ln == "":
        break
    elif me := re.match(r"load (\w+)", ln):
        Block.load(me.group(1))
    elif me := re.match(r"new (\w+)", ln):
        Block.new(me.group(1))
    elif me := re.match(r"cube (\d+)", ln):
        cube(int(group(1)), int(group(2)))
    elif me := re.match(r"cube (\d+) (\d+) (\d+)", ln):
        put(int(me.group(1)), int(me.group(2)), int(me.group(3)))
    elif ln == "done":
        done()
    elif me := re.match(r"output (\w+)", ln):
        Block.output(me.group(1))
    else:
        print(help)