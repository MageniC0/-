block_pixels = [[[[[[0, 0, 0, 0] for u in range(13)] for v in range(13)] for x in range(4)] for y in range(4)] for z in range(4)]  # I
graph = [[[0, 0, 0, 0] for i in range(49)] for j in range(49)]  # O

def pos(x, y, z):
    m = 18 - 6 * x + 6 * y
    n = 24 + 2 * x + 2 * y - 8 * z
    return (m, n)

# 起笔坐标
m = None
n = None

for z in range(4):
    for y in range(4):
        for x in range(4):
            m, n = pos(x, y, z)
            for j in range(13):
                for i in range(13):
                    for k in range(4):
                        graph[n + j][m + i][k] = block_pixels[z][y][x][j][i][k]  # 避免直接赋值

