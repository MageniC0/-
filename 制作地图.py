import json
import re

help = """[help]
load [name]: 编辑已有地图
new [name]: 新建地图
draw [n]: 指定要放置的方块
point [x] [y] [z]: 在指定位置放置或删除方块
clean: 删除模式或取消删除模式
done: 完成编辑
output [name]: 另存文件
"""

class Block:
    def __init__(self):
        self.block = []
        self.name = ""
    
    def load(self):
        with open(self.name, "r") as f:
            self.block = json.load(f)
    
    def new(self):
        self.block = [[[0 for x in range(4)] for y in range(4)] for z in range(4)]
    
    def set_name(self, name):
        self.name = "tr/" + name

    def done(self):
        print(f"已将地图保存至{self.name}")
    
class Mon:
    def __init__(self):
        self.draw_ = 0
        self.clean_ = 0

    def draw(self, n):
        self.draw_ = n

    def clean(self):
        if self.clean_ == 0:
            self.clean_ = 1
        else: 
            self.clean_ = 0










while True:
    ln = input("_")
    if ln == "":
        break
    elif me := re.match(r"load (\w+)", ln):
        Block.load(me.group(1))
    elif me := re.match(r"new (\w+)", ln):
        Block.new(me.group(1))
    elif me := re.match(r"draw (\d+)", ln):
        Mon.draw(int(group(1)))
    elif me := re.match(r"point (\d+) (\d+) (\d+)", ln):
        Mon.point(int(me.group(1)), int(me.group(2)), int(me.group(3)))
    elif ln == "clean": 
        Mon.clean()
    elif ln == "done":
        Block.done()
    elif me := re.match(r"output (\w+)", ln):
        Block.output(me.group(1))
    else:
        print(help)