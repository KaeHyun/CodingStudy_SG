# 숨바꼭질
INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF]*n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for a in range(n):
    for b in range(n):
        if a == b:
            graph[a][b] = 0

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

maximum = 0
for i in graph[0]:
    if i != INF:
        maximum = max(maximum, i)

print(f'{graph[0].index(maximum)+1} {maximum} {graph[0].count(maximum)}')

