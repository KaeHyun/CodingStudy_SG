# 백준 18352 번
# 문제 요약: 도시의 개수와 연결된 정보가 주어짐 -> 주어진 거리 정보에 부합하는 모든 도시들을 출력!

from collections import deque
import sys

# N: 도시의 개수, M: 도로의 개수, K: 거리 정보, X: 출발 도시의 번호

input = sys.stdin.readline
N, M, K, X = map(int, input().split())

city_map = [[] for _ in range(N+1)]

distance = [-1] * (N+1) # 거리 계산
distance[X] = 0

for _ in range(M):
    a, b = map(int, input().split())
    city_map[a].append(b)

# BFS 시작
queue = deque([X]) # 시작 도시 
while queue:
    current_city = queue.popleft()
    for nxt_city in city_map[current_city]:
        if distance[nxt_city] == -1: # 방문한적 없는 연결 노드라면
            queue.append(nxt_city)
            distance[nxt_city] = distance[current_city] + 1

Flag = False

for i in range(N+1):
    if distance[i] == K:
        print(i)
        Flag = True

if Flag == False:
    print(-1)
