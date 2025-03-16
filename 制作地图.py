import json
import re

class Block:
    def __init__(self):
        self.block = []
        self.name = ""
    
    def set_name(self, name):
        self.name = "tr/" + name + ".json"
    
    def load(self, name):
        self.set_name(name)
        with open(self.name, "r") as f:
            self.block = json.load(f)
    
    def new(self, name):
        self.set_name(name)
        self.block = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
        self.save()
    
    def save(self):
        with open(self.name, "w") as f:
            json.dump(self.block, f)
    
    def output(self, name):
        with open(name, "w") as f:
            json.dump(self.block, f)
    
    def done(self):
        print(f"地图保存至{self.name}")

class Mon:
    def __init__(self, block):
        self.draw_ = 0
        self.clean_ = 0
        self.block_ = block
    
    def draw(self, n):
        self.draw_ = n
    
    def point(self, x, y, z):
        if self.clean_:
            self.block_.block[z][y][x] = 0
        else:
            self.block_.block[z][y][x] = self.draw_
        self.block_.save()
    
    def clean(self):
        self.clean_ = 1 - self.clean_

class Starlit:
    def __init__(self):
        self._block = Block()
        self._mon = Mon(self._block)
        self.ln = ""
        self.help = """[help]____________________________
load [name]: 导入地图
new [name]: 新建地图
draw [n]: 设置的笔刷
point [x][y][z]: 放置/移除方块
clean: 删除模式/取消删除模式
done: 退出程序
output [name]: 导出
__________________________________
"""
    
    def main(self):
        while True:
            self.ln = input("_").strip()
            if not self.ln:
                continue
            
            if cmd := re.match(r"load (\w+)", self.ln):
                self._block.load(cmd.group(1))
            elif cmd := re.match(r"new (\w+)", self.ln):
                self._block.new(cmd.group(1))
            elif cmd := re.match(r"draw (\d+)", self.ln):
                self._mon.draw(int(cmd.group(1)))
            elif cmd := re.match(r"point (\d+) (\d+) (\d+)", self.ln):
                x, y, z = map(int, cmd.groups())
                self._mon.point(x, y, z)
            elif self.ln == "clean":
                self._mon.clean()
            elif self.ln == "done":
                self._block.done()
                break
            elif cmd := re.match(r"output (\w+)", self.ln):
                self._block.output(cmd.group(1))
            else:
                print(self.help)

_tr = Starlit()
_tr.main()
