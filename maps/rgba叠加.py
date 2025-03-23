def mix(r1, g1, b1, a1, r2, g2, b2, a2):
    a = a1 + a2 * (1 - a1 / 255)
    if a == 0:
        return [0, 0, 0, 0]
    f = a1 / a
    r = int(r1 * f + r2 * (1 - f))
    g = int(g1 * f + g2 * (1 - f))
    b = int(b1 * f + b2 * (1 - f))
    return [r, g, b, int(a)]

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
                        pixel1 = block_pixels[z][y][x][j][i]
                        pixel2 = graph[n + j][m + i]
                        mixed_pixel = mix(pixel1[0], pixel1[1], pixel1[2], pixel1[3],
                                          pixel2[0], pixel2[1], pixel2[2], pixel2[3])
                        graph[n + j][m + i] = mixed_pixel
