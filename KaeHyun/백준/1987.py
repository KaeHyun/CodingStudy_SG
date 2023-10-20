import sys 

input = sys.stdin.readline

# 상 좌 하 우 
dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]


R, C = map(int, input().split())
abc_map = []

for _ in range(R):
    abc_map.append(list(input()))


curr_abc = set()
answer = 0

def DFS(x, y, count):
    global answer

    # if count <= answer:
    #     return 

    answer = max(answer, count)

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy # 새로운 곳
        #print(abc_map[nx][ny])
        if 0<= nx < R and 0<=ny<C and not abc_map[nx][ny] in curr_abc:
            # 격자 내부에 존재하고  방문한 적 없고 아직 나오지 않은 알파벳이라면, 
            curr_abc.add(abc_map[nx][ny])
            DFS(nx, ny, count +1)
            curr_abc.remove(abc_map[nx][ny])


curr_abc.add(abc_map[0][0])
DFS(0,0,1)

print(answer)