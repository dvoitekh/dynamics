import math
import random

INF = 10000000000000
K = 1
M = 0.0001
N = 8 # includes one extra vertice to transform hamilton cycle into path, which is finally removed from the result
points = [[random.randint(1, 100), random.randint(1, 100)] for i in range(N)] + [[-10, -10]] # points[N] - point after operations
distances = [[math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) for j in range(N + 1)] for i in range(N + 1)]
d = [[INF for j in range(2 ** N)] for i in range(N)]
d[0][0] = 0

def find_angle(a, b, c):
    if a == b or a == c or b == c:
        return 0
    x1 = points[a][0] - points[b][0]
    x2 = points[c][0] - points[b][0]
    y1 = points[a][1] - points[b][1]
    y2 = points[c][1] - points[b][1]
    d1 = math.sqrt(x1 * x1 + y1 * y1)
    d2 = math.sqrt(x2 * x2 + y2 * y2)
    return 0 if not(d1 and d2) else math.acos((x1 * x2 + y1 * y2) / (d1 * d2)) / math.radians(1)

angles = [[[find_angle(a, b, c) for c in range(N + 1)] for b in range(N + 1)] for a in range(N + 1)]

def w(prev, i, j):
    if prev == i or prev == j or i == j or not distances[i][j]:
        return 0
    return K * distances[i][j] + M * angles[prev][i][j]

def find_cheapest(prev, i, mask):
    if d[i][mask] != INF:
        return d[i][mask]
    for j in range(N):
        if w(prev, i, j) and 1 << j & mask:
            d[i][mask] = min(d[i][mask], find_cheapest(i, j, mask ^ 1 << j) + w(prev, i, j))
    return d[i][mask]

def start():
    ans = find_cheapest(N, 0, 2 ** N - 1)
    return ans

def find_way():
    mask = 2 ** N - 1
    prev = N
    i = 0
    path = [prev, i]
    while mask != 0:
        for j in range(N):
            if w(prev, i, j) and 1 << j & mask and math.fabs(d[i][mask] - (d[j][mask ^ 1 << j] + w(prev, i, j))) < 0.01:
                path.append(j)
                prev = i
                i = j
                mask ^= 1 << j
                break
    print(path)

if __name__ == '__main__':
    start()
    find_way()
