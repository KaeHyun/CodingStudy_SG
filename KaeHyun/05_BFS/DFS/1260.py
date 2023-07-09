#DFS와 BFS

#Python은 기본적으로 문자로 입력을 받는다.
#공백으로 들어오는 정수 입력 각각 입력받기 
# N : 정점의 개수 / M : 간선의 개수 / V :  탐색을 시작할 정점의 번호
from collections import deque

N, M, V = map(int, input().split())

graph = [[0]*(N+1) for _ in range(N+1)]
dfs_visit = [0] *(N+1)
bfs_visit = [0] *(N+1)

# 그래프 연결 관계를 입력으로 받기 -> 연결:1 연결 X:0
for i in range(M):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1 

#print(graph)

def DFS(start):
    dfs_visit[start] = 1 # 탐색 시작 지점 1로 변경
    print(start, end=' ')
    for i in range(N+1):
        if(dfs_visit[i]== 0 and graph[start][i] == 1): #방문한 적 없고 연결 되어있다면 다시 DFS 호출 (재귀)
            DFS(i)
    
def BFS(start): #큐 자료구조 이용
    queue = deque([start])#탐색 시작 노드 큐에 삽입

    bfs_visit[start] =1
    while queue: # queue가 빌때까지
        v = queue.popleft()
        print(v, end=" ")
        for i in range(N+1):
            if graph[v][i] == 1 and bfs_visit[i] == 0:
                queue.append(i)
                bfs_visit[i] = 1 
                
    
DFS(V)
print()
BFS(V)