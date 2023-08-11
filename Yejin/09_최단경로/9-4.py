# 미래 도시
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n*2+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

x, k = map(int, input().split())

def dijkstra(start):
    q = []
    distance = [INF] * (n+1)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        cost, now = heapq.heappop(q)
        if distance[now] < cost:
            continue
        for i in graph[now]:
            if cost + i[1] < distance[i[0]]:
                distance[i[0]] = cost + i[1]
                heapq.heappush(q, (cost + i[1], i[0]))

    return distance

distance1 = dijkstra(1)
distance2 = dijkstra(k)

if distance1[k] == INF or distance2[x] == INF:
    print(-1)
else:
    print(distance1[k] + distance2[x])