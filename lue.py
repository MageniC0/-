help = """[help]
sh: 检查目录
ch: 检查资源包
tr: 检查地图册
pt: 修改路径
"""

import os

start = os.getcwd()

def lue(lm):
    d0 = []
    d1=os.path.abspath(lm)
    for d2, _, d3 in os.walk(d1):
        d4=d2.replace(d1, '').count(os.sep)
        d0.append("|   " * d4+f"[{os.path.basename(d2)}]\n")
        d0.extend("|   " * (d4 + 1)+f"{d6}\n" for d6 in d3)
    print("".join(d0))

while True:
    print()
    ln = input("_")
    if ln == "":
        break
    elif ln == "sh":
        lue(start + "/")
    elif ln == "ch":
        lue(start + "/ch/")
    elif ln == "tr":
        lue(start + "/tr/")
    elif ln == "pt":
        with open("pt.json", 'r') as file:
            print(file.read())
    else:
        print(help)