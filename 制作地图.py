import json
import re

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









class Starlit:
    def __init__(self):
        self.ln = ""
        self.help = """[help]
        load [name]: 编辑已有地图
        new [name]: 新建地图
        draw [n]: 指定要放置的方块
        point [x] [y] [z]: 在指定位置放置或删除方块
        clean: 删除模式或取消删除模式
        done: 完成编辑
        output [name]: 另存文件
        """

    def load():
        pass

    def new():
        pass

    def draw():
        pass

    def point():
        pass

    def clean():
        pass

    def done():
        pass

    def output():
        pass
    
    def main(self):
        while True:
            self.ln = input("_")
            if self.ln == "":
                break
            elif me := re.match(r"load (\w+)", self.ln):
                self.load(me.group(1))
            elif me := re.match(r"new (\w+)", self.ln):
                self.new(me.group(1))
            elif me := re.match(r"draw (\d+)", self.ln):
                self.draw(int(me.group(1)))
            elif me := re.match(r"point (\d+) (\d+) (\d+)", self.ln):
                self.point(int(me.group(1)), int(me.group(2)), int(me.group(3)))
            elif self.ln == "clean": 
                self.clean()
            elif self.ln == "done":
                self.done()
            elif me := re.match(r"output (\w+)", self.ln):
                self.output(me.group(1))
            else:
                print(help)