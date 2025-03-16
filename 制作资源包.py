#打开一个图片，然后转化为资源包
from PIL import Image
import json

n = 0
image = Image.open("src/laer.png")
graph = [[[(0, 0, 0, 0) for i in range(13)] for j in range(13)] for n in range(16)]
for y in range(4):
    for x in range(4):
        for j in range(13):
            n = 4 * y + x
            for i in range(13):
                graph[n][j][i] = image.getpixel((16 * y + j, 16 * x + i))

with open("chc/laer.json", "w") as f:
    json.dump(graph, f)