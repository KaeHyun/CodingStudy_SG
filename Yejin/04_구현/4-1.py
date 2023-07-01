n = int(input())
route = list(map(str, input().split()))

rr = ['L', 'R', 'U', 'D']
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

x, y = 0, 0
for r in route:
    nx = x + dx[rr.index(r)]
    ny = y + dy[rr.index(r)]
    if 0<=nx<=n and 0<=ny<=n:
        x, y = nx, ny

print(f'{y+1} {x+1}')