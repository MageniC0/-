import copy

tr = [[[0 for x in range(4)] for y in range(4)] for z in range(4)]  # I
chc = [[[[0, 0, 0, 0] for u in range(13)] for v in range(13)] for n in range(16)]  # I
block_pixels = [[[[[[0, 0, 0, 0] for u in range(13)] for v in range(13)] for x in range(4)] for y in range(4)] for z in range(4)]  # O

ch = None  # 影

for z in range(4):
    for y in range(4):
        for x in range(4):
            if tr[z][y][x] != 0:
                ch = chc[tr[z][y][x]]
                block_pixels[z][y][x] = copy.deepcopy(ch) # 硬拷贝