from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, ice_map):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and ice_map[ny][nx] == 0:
                ice_map[ny][nx] = 1
                queue.append((nx, ny))

    return ice_map

n, m = map(int, input().split())
ice_map = []
res = 0

for i in range(n):
    ice_map.append([int(x) for x in input()])

for i in range(n):
    for j in range(m):
        if ice_map[i][j] == 0:
            ice_map = dfs(j, i, ice_map)
            res += 1

print(res)