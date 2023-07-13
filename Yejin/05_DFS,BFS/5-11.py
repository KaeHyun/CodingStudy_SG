from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = map(int, input().split())
miro = []

for i in range(n):
    miro.append([int(x) for x in input()])

queue = deque()
queue.append((0, 0))

while queue:
    x, y = queue.pop()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and miro[ny][nx] != 0:
            miro[ny][nx] = miro[y][x] + 1
            queue.append((nx, ny))

print(miro[n-1][m-1])