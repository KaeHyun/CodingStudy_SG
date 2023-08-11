# 정확한 순위
# 모든 길로 가는 게 가능하면 됨
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if (graph[i][j] != 0 and graph[i][j] != INF) or (graph[j][i] != 0 and graph[j][i] != INF):
            cnt +=1
    if cnt == n-1:
        result += 1

print(result)