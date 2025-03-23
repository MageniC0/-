def pos(x, y, z):
    m = 18 - 6 * x + 6 * y
    n = 24 + 2 * x + 2 * y - 8 * z
    return (m, n)

m, n = pos(1, 2, 3)
print(m, n)