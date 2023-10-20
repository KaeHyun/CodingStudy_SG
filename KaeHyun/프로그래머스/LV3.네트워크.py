


def DFS(computer_num, computers, visited, n):
    visited[computer_num] = 1 # 해당 컴퓨터 방문처리 
    
    for i in range(n):
        if computers[computer_num][i] == 1 and not visited[i]:
            DFS(i, computers, visited, n)
                

# 연결되면 하나의 네트워크 
def solution(n, computers):
    ans = 0 
    visited = [0] *n # DFS에서 사용할 방문 체크 
    # DFS의 시작점이 딱히 정해져 있지 않다... ! 
    for i in range(n): 
        if not visited[i]:
            DFS(i, computers, visited, n)
            ans +=1
    print(ans)

    return ans

solution(	3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
#solution(4, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

