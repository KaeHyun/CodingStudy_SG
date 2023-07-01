from collections import deque

# 북 동 남 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

n, m = map(int, input().split())
x, y, d = map(int, input().split())
queue = deque()
queue.append((x, y))

game_map = []
for i in range(n):
    game_map.append(list(map(int, input().split())))

game_map[y][x] = 1
res = 1
while queue:
    x, y = queue.pop()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<m and 0<=ny<n and game_map[ny][nx] == 0:
            game_map[ny][nx] = 1
            queue.append((nx, ny))
            res += 1

print(res)