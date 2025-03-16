#检查某个方块的某个位置的像素值
import json
import re

help = """[help]
check [n] [u] [v]: 检查第n个方块的(u, v)像素值
"""

with open("chc/laer.json", "r") as f:
    chc = json.load(f)

def check(n, u, v):
    rgba = chc[n][u][v]
    print(f"r = {rgba[0]}\ng = {rgba[1]}\nb = {rgba[2]}\na = {rgba[3]}")

while True:
    ln = input("_")
    if ln == "":
        break
    elif me := re.match(r"check (\d+) (\d+) (\d+)", ln):
        check(int(me.group(1)), int(me.group(2)), int(me.group(3)))
    else:
        print(help)