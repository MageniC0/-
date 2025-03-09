from PIL import Image
import json

n = 0
image = Image.open("input.png")
graph = [[[(0, 0, 0, 0) for i in range(13)] for j in range(13)] for n in range(256)]
for y in range(16):
    for x in range(16):
        for j in range(13):
            n = 16 * y + x
            for i in range(13):
                graph[n][j][i] = image.getpixel((16 * y + j, 16 * x + i))

with open("chc.json", "w") as f:
    json.dump(graph, f)