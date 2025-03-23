import re
import json
from PIL import Image
import copy

help = '''[help]
输入指令以执行操作。
按下回车键以执行。
chc [name] : 指定资源包
tr [name] : 指定地图
output [name] : 制作
在空行按下回车键以退出。
'''

class F:
    def __init__(self, type):
        self.name = None
        self.data = None
        self.type = type

    def load(self):
        print("load " + self.name)
        with open(self.name, "r") as f:
            self.data = json.load(f)

# 线性映射
def pos(x, y, z):
    m = 18 - 6 * x + 6 * y
    n = 24 + 2 * x + 2 * y - 8 * z
    return (m, n)

# rgba混合
def mix(r1, g1, b1, a1, r2, g2, b2, a2):
    a = a1 + a2 * (1 - a1 / 255)
    if a == 0:
        return [0, 0, 0, 0]
    f = a1 / a
    r = int(r1 * f + r2 * (1 - f))
    g = int(g1 * f + g2 * (1 - f))
    b = int(b1 * f + b2 * (1 - f))
    return [r, g, b, int(a)]

class Dvc:
    def __init__(self):
        self.chc_ = F("chc")
        self.tr_ = F("tr")
    
    def dvc(self):
        while True:
            ln = input("_")
            if ln == "":
                break
            elif cmd := re.match(r"chc (\w+)", ln):
                self.chc(cmd.group(1))
            elif cmd := re.match(r"tr (\w+)", ln):
                self.tr(cmd.group(1))
            elif cmd := re.match(r"output (\w+)", ln):
                self.output(cmd.group(1))
            else:
                print(help)
    
    def chc(self, name):
        self.chc_.name = "chc/" + name + ".json"
        self.chc_.load()

    def tr(self, name):
        self.tr_.name = "tr/" + name + ".json"
        self.tr_.load()

    def output(self, name):
        block_pixels = [[[[[[0, 0, 0, 0] for u in range(13)] for v in range(13)] for x in range(4)] for y in range(4)] for z in range(4)]
        graph = [[[0, 0, 0, 0] for i in range(49)] for j in range(49)]

        for z in range(4):
            for y in range(4):
                for x in range(4):
                    if self.tr_.data[z][y][x] != 0:
                        ch = self.chc_.data[self.tr_.data[z][y][x]]
                        block_pixels[z][y][x] = copy.deepcopy(ch)

        m = None
        n = None
        for z in range(4):
            for y in range(4):
                for x in range(4):
                    m, n = pos(x, y, z)
                    for j in range(13):
                        for i in range(13):
                            for k in range(4):
                                pixel1 = block_pixels[z][y][x][j][i]
                                pixel2 = graph[n + j][m + i]
                                mixed_pixel = mix(pixel1[0], pixel1[1], pixel1[2], pixel1[3], pixel2[0], pixel2[1], pixel2[2], pixel2[3])
                                graph[n + j][m + i] = mixed_pixel

        image = Image.frombytes('RGBA', (49, 49), bytes([channel for row in graph for pixel in row for channel in pixel]))
        image.save(name + ".png")

laer = Dvc()
laer.dvc()