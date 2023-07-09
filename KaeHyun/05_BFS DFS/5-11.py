# 미로 탈출

# 문제 요약 : 동빈이 시작 위치 (1,1) 미로의 출구 (N, M) 괴물이 있는 부분 0 없는 부분 1
#            이때, 동빈이가 움직여야하는 최소 칸의 개수 (시작 칸 & 마지막 칸 전부 포함) 

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111


from collections import deque

N, M = map(int, input().split())
maze_graph = []
answer =0 

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    maze_graph.append(list(map(int, input())))
#print(maze_graph)

queue = deque()

def BFS(a, b):
    global answer
    queue.append((a,b)) #탐색 시작 노드 큐에 삽입

    maze_graph[a][b] = 0
    #print(queue)

    while queue:
        x, y = queue.popleft()
        answer +=1
        for i in range(4):
            xt = x + dx[i]
            yt = y + dy[i]
            if xt < 0 or yt < 0 or xt >= N or yt >=M:
                continue

            if maze_graph[xt][yt] == 1 and xt >= x and yt >= y: # 몬스터가 없고 오른쪽 아래인 위치일 때만
                queue.append((xt, yt))
                maze_graph[xt][yt] = 0



BFS(0,0)
print(answer)