import re
import json
from PIL import Image

help = '''[help]
chc [name] : 指定资源包
tr [name] : 指定地图
output [name] : 制作
按下回车键以退出
'''

class F:
    def __init__(self):
        self.name = None
        self.data = None

    def open_file(self):
        with open(self.filename, "r") as f:
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
        self.chc = F()
        self.tr = F()

def chc(name):
    print(f"chc for {name}")
    # 导入chc

def tr(name):
    print(f"tr for {name}")
    # 导入tr

def output(name):
    print(f"output for {name}")
    # 生成block_pixels
    # 生成graph
    # 导出


while True:
    ln = input("_")
    if ln == "":
        break
    elif cmd := re.match(r"chc (\w+)", ln):
        chc(cmd.group(1))
    elif cmd := re.match(r"tr (\w+)", ln):
        tr(cmd.group(1))
    elif cmd := re.match(r"output (\w+)", ln):
        output(cmd.group(1))
    else:
        print(help)