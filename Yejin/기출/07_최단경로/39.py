# 화성 탐사
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def find_route(route, n):
    distance = [[INF] * n for _ in range(n)]
    q = []
    heapq.heappush(q, (route[0][0], 0, 0))
    distance[0][0] = route[0][0]
    while q:
        energy, x, y = heapq.heappop(q)
        if distance[x][y] < energy:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = energy + route[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
    return distance[n-1][n-1]


t = int(input())
for _ in range(t):
    n = int(input())
    route = []
    for _ in range(n):
        route.append(list(map(int, input().split())))
    print(find_route(route, n))

    