#음료수 얼려먹기

# 문제 요약: N X M 크기의 얼음 틀 존재 => 0이라면 구멍이 뚫림 / 1이라면 칸막이 존재 
#           상, 하, 좌, 우로 붙어있으면 연결된 걸로 간주
# 4 5
# 00110
# 00011
# 11111
# 00000

N, M = map(int, input().split())

ice_graph = []
answer = 0

for _ in range(N):
    ice_graph.append(list(map(int, input())))

# visit 리스트를 굳이 만들지 않고 ice_graph 자체에서 변경하는 방법으로 

def DFS(x, y):

    if x<0 or y<0 or x >= N or y>= M: #좌표를 벗어나면 return
        return -1
    if ice_graph[x][y] == 0: 
        ice_graph[x][y] =1 # 얼음을 만들 수 있으면, 방문한 걸로 변경

        #재귀적으로 상 하 좌 우 확인
        DFS(x-1, y)
        DFS(x+1, y)
        DFS(x, y-1)
        DFS(x, y+1)

        return 1
    return -1

for i in range(0, N):
    for j in range(0, M):
        v = DFS(i, j)
        if v == 1:
            answer +=1
print(answer)




