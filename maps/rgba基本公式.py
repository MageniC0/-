def mix(r1, g1, b1, a1, r2, g2, b2, a2):
    a = a1 + a2 * (1 - a1 / 255)
    if a == 0:
        return [0, 0, 0, 0]
    f = a1 / a
    r = int(r1 * f + r2 * (1 - f))
    g = int(g1 * f + g2 * (1 - f))
    b = int(b1 * f + b2 * (1 - f))
    return [r, g, b, int(a)]

print(mix(22, 90, 2, 2, 0, 0, 0, 2)) 
