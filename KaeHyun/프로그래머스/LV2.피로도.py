# 던전 탐험을 시작하기 위해 필요한 : 최소 피로도
# 던전 탐험 마치면 소모되는: 소모 피로도 

answer = 0 

def DFS(k, d_count, dungeons, visited):
    global answer 
    if d_count > answer:
        answer = d_count

    for i in range(len(dungeons)):
        start_p, end_p = dungeons[i]
        if not visited[i] and start_p <=k:
            # 방문한 적 없고, 유저의 남아있는 체력보다 최소 피로도가 낮거나 같을 때만 
            visited[i] =1
            DFS(k-end_p, d_count+1, dungeons, visited)
            visited[i] = 0

def solution(k, dungeons):

    # 시작은 (초기 피로도, 정답)
    visited = [0] * len(dungeons) # 던전 방문 기록 (DFS 이용)

    DFS(k, 0, dungeons, visited)
    
    #print(answer)
    return answer

solution(80, [[80,20],[50,40],[30,10]])