import math
import random

INF = 10000000000000
N = 10
points = [[random.randint(1, 10), random.randint(1, 10)] for i in range(N)]
d = [[INF for j in range(2 ** N)] for i in range(N)]
d[0][0] = 0

def w(i, j):
    return math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)

def find_cheapest(i, mask):
    if d[i][mask] != INF:
        return d[i][mask]
    for j in range(N):
        if w(i, j) and 1 << j & mask:
            d[i][mask] = min(d[i][mask], find_cheapest(j, mask ^ 1 << j) + w(i, j))
    return d[i][mask]

def start():
    ans = find_cheapest(0, 2 ** N - 1)
    return ans

def find_way():
    i = 0
    mask = 2 ** N - 1
    path = [0]
    while mask != 0:
        for j in range(N):
            if w(i, j) and 1 << j & mask and d[i][mask] == d[j][mask ^ 1 << j] + w(i, j):
                path.append(j)
                i = j
                mask ^= 1 << j
                break
    print(path)

start()
find_way()
