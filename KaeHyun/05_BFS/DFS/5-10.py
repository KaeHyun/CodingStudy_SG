#음료수 얼려먹기

# 문제 요약: N X M 크기의 얼음 틀 존재 => 0이라면 구멍이 뚫림 / 1이라면 칸막이 존재 
#           상, 하, 좌, 우로 붙어있으면 연결된 걸로 간주
# 4 5
# 00110
# 00011
# 11111
# 00000

N, M = map(int, input().split())

graph = []

for i in range(N):
    graph.append(list(map(int, input()))) #공백으로 구분이 안되니까 입력 받아서 리스트로

def DFS(a, b): # 상하좌우 전부 탐색

    if a< 0 or b < 0 or a >= N or b >= M:
        return -1
    
    if graph[a][b] == 0 : # 구멍이 뚫림(== 아직 방문하지 않음)
        graph[a][b] = 1 # 방문함으로 변경
        # 상하좌우 탐색
        DFS(a+1, b)
        DFS(a-1, b)
        DFS(a, b-1)
        DFS(a, b+1) 
        return 1

    return -1

answer = 0 
for i in range(N):
    for j in range(M):
        if DFS(i, j) == 1:
            answer+=1
        
print(answer)




