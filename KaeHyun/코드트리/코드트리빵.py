# 2022 하반기 오후 1번 문제 (골드 2)
# 이동하는 도중 동일한 칸에 둘 이상의 사람이 위치하게 되는 경우 역시 가능함에 유의
from collections import deque

n, m = map(int, input().split())

people_dict = {} # 각 사람이 가고 싶어하는 편의점의 위치 
people_pos = [(-1,-1)]*m # 사람 위치 정보 관리
base_cvs=[] # 베이스 캠프 & 편의점 표시

# 베이스캠프: 1 / 편의점: 2 / 못가는 곳: -1
for _ in range(n):
    base_cvs.append(list(map(int, input().split())))

for i in range(m):
    x, y= map(int, input().split())
    base_cvs[x-1][y-1] = 2
    people_dict[(i)] = [x-1, y-1]

# 우선순위:  ↑(상), ←(좌), →(우), ↓(하)  
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

visited = [[0]* n for _ in range(n)] # BFS에 사용할 방문 여부 
route = [[0]* n for _ in range(n)] # BFS에 사용할 최단 거리 계산  

def in_range(x,y):
    if x>=0 and x < n and y>=0 and y<n:
        return True
    else:
        return False

def check_go(x, y):
    # 격자 내에 존재 / 지나갈 수 있는 / 방문한적 없는
    if in_range(x,y) and base_cvs[x][y] != -1  and visited[x][y] != 1:
        return True
    else:
        return False

def short_path(start_pos):
    # BFS 이용
    x, y = start_pos[0], start_pos[1]
    # 초기화
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0
            route[i][j] = 0

    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    route[x][y] = 1

    while queue:
        x,y = queue.popleft()

        for dxx, dyy in zip(dx, dy):
            nx, ny = x + dxx, y + dyy
            # 갈 수 있는 경우에만 간다. 
            if check_go(nx, ny):
                queue.append((nx,ny))
                visited[nx][ny] = 1
                route[nx][ny] = route[x][y] + 1


def simualte():
    # Step 1. 격자에 있는 사람들 모두 본인이 원하는 편의점으로 최단거리로 1칸
    for i in range(m): 
        tmp = (people_dict[i][0], people_dict[i][1])
        if people_pos[i] == (-1, -1) or people_pos[i] == tmp: # 아직 사람이 격자 안으로 들어오지 않음
            continue
        short_path(people_dict[i]) # 편의점 위치에서 시작해서 최단 거리 찾기 

        px, py = people_pos[i] # 현재 사람의 위치

        # 현재 사람의 위치에서부터 4 방향 중 가장 작은 값(=짧은거리)으로 이동
        min_dis = 9999 
        min_px, min_py = -1, -1
        for dxx, dyy in zip(dx, dy):
            npx, npy = px + dxx, py + dyy
            if in_range(npx, npy) and visited[npx][npy] and min_dis > route[npx][npy]:
                min_dis = route[npx][npy]
                min_px, min_py = npx, npy
        people_pos[i] = (min_px, min_py)

    # Step 2. 편의점 도착 시 , 해당 편의점에서 멈춤 그러면 해당 칸을 다른 사람들은 지나갈 수 없음
    # ->  격자에 있는 사람들이 모두 이동한 뒤에 해당 칸을 지나갈 수 없어짐에 유의

    for i in range(m):
        goal_x, goal_y = people_dict[i]
        curr_x, curr_y = people_pos[i]
        if goal_x == curr_x and goal_y == curr_y:
            # 편의점에 도착
            base_cvs[curr_x][curr_y] = -1
            
    # Step 3. 현재 시간이 t분이고 t ≤ m를 만족한다면, t번 사람은 자신이 가고 싶은 편의점과 
    # 가장 가까이 있는 베이스 캠프에 | 행이 작은 베이스캠프, 행이 같다면 열이 작은 베이스 캠프
    if time > m: 
        # 시간이 m보다 크면 모든 사람들이 베이스 캠프에 도착했을 것
        return 

    short_path(people_dict[time-1]) # t 번 사람이 가고 싶은 편의점과 가장 가까운 베이스 캠프 

    min_base = 9999
    for i in range(n):
        for j in range(n):
            if base_cvs[i][j] == 1 and min_base > route[i][j] and visited[i][j]:
                min_base = route[i][j] 
                base = (i,j)
    bx, by = base
    people_pos[time-1] = (bx, by)
    base_cvs[bx][by] = -1

def check_end():
    # 모든 사람이 편의점에 도착했는지 확인하는 함수 
    # 한 사람이라도 도착 안하면 안됨 
    for key, value in people_dict.items():
        x, y = value[0], value[1]
        if people_pos[key] != (x,y):
            return False    
    return True
        
# 현재 시간 
time = 0

while True:
    time +=1
    simualte()
    if check_end():
        break
print(time)