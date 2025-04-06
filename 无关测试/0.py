import numpy as np

def householder_qr(A):
    m, n = A.shape
    Q = np.eye(m)
    R = A.copy()

    for k in range(n):
        x = R[k:, k]
        e1 = np.zeros_like(x)
        e1[0] = np.linalg.norm(x)
        v = x + np.sign(x[0]) * e1
        v = v / np.linalg.norm(v)

        H = np.eye(m)
        H[k:, k:] -= 2.0 * np.outer(v, v)

        Q = np.dot(Q, H)
        R = np.dot(H, R)

    return Q, R

A = np.array([[12, -51, 4],
              [6, 167, -68],
              [-4, 24, -41]], dtype=float)

Q, R = householder_qr(A)

print("Q 矩阵:")
print(Q)
print("\nR 矩阵:")
print(R)

print("\n验证 A = QR:")
print(np.dot(Q, R))