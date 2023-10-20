# N X M  격자 , K = 턴 수
from collections import deque

n, m, k = map(int, input().split())
grid =[]
for _ in range(n):
    grid.append(list(map(int, input().split())))

attack_memo= [[0]*m for _ in range(n)] # 공격 기록 

visited = [[0]*m for _ in range(n)]
route = [[0]*m for _ in range(n)]
# 우선순위: 우 상 좌 하 
dxs = [0, -1, 0, 1]
dys = [1, 0, -1, 0]

def select_attacker():
    # 가장 약한 포탑을 공격자로 선정
    lowest = (9999, 9999, -9999, -9999) # 공격력, 최근 공격, 행+열의 합이 가장 큰, 열의 값이 가장 큰 
    attack = 9999

    for i in range(n):
        for j in range(m):
            if grid[i][j] <= attack and grid[i][j] != 0: 
                attack = grid[i][j]
                recent = attack_memo[i][j]
                row_col = i + j
                col = j
                tmp = (attack, recent, -row_col, -col)
                if tmp <lowest:
                    lowest = tmp
    return lowest

def select_high(x, y):
    # 공격대상자 선정
    highest = (-99999, 9999, 9999, 9999)
    attack = -1

    for i in range(n):
        for j in range(m):
            if grid[i][j] >= attack and grid[i][j] != 0 and (i,j) != (x,y): 
                attack = grid[i][j]
                recent = attack_memo[i][j]
                row_col = i + j
                col = j
                tmp = (attack, -recent, -row_col, -col)
                if tmp >= highest:
                    highest = tmp
    return highest

def in_range(x, y):
    x = x % n
    y = y % m 
    return x, y
    
def BFS(ox, oy):
    # 초기화
    for i in range(n):
        for j in range(m):
            visited[i][j] = 0
            route[i][j] = 0 

    queue = deque()
    queue.append((ox,oy))
    visited[ox][oy] = 1 
    route[ox][oy] = 1 

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            nx, ny = in_range(nx, ny)
            if grid[nx][ny] !=0 and visited[nx][ny] == 0:
                # 격자 범이 내에 존재하고 부서진 포탑이 위치하지 않고 방문한적 없는 곳 이라면
                queue.append((nx, ny))
                visited[nx][ny] = 1
                route[nx][ny] = route[x][y] +1

def bomb_attack(att_x, att_y, obj_x, obj_y):
    global damage_memo, grid

    damage = grid[att_x][att_y]

    grid[obj_x][obj_y] -= damage # 직격탄

    damage_memo.append((obj_x, obj_y))

    ddx = [-1 , -1, -1, 0, 1, 1, 1, 0]
    ddy = [-1, 0, 1, 1, 1, 0, -1, -1]
    half_damage = damage//2
    
    for dx, dy in zip(ddx, ddy):
        nx, ny = obj_x + dx, obj_y +dy
        nx, ny = in_range(nx, ny)
        if (nx, ny) == (att_x, att_y): # 해당자는 영향받지 않음
            grid[nx][ny]+=0
        elif grid[nx][ny] != 0:
            grid[nx][ny] -= half_damage
            damage_memo.append((nx, ny))

def laser_attack(att_x, att_y, obj_x, obj_y):
    # 공격당하는 포탑 기준으로 최단 거리 계산!
    global damage_memo, grid

    BFS(obj_x, obj_y)

    tmp = 9999
    laser_route = []
    ori_x, ori_y = att_x, att_y
    laserQ = deque()
    laserQ.append((ori_x, ori_y))

    while laserQ:
        x, y = laserQ.popleft()
        if x == obj_x and y == obj_y:
            break
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            nx, ny = in_range(nx,ny)
            if route[nx][ny] < tmp and visited[nx][ny] == 1:
                tmp = route[nx][ny]
                laserQ.append((nx, ny))
                laser_route.append((nx, ny))

    if len(laser_route) == 0:
        # 레이저 공격이 가능한 경로가 없다면, 
        bomb_attack(ori_x, ori_y, obj_x, obj_y)
    else:
        attack = grid[att_x][att_y] # 공격력
        last_x, last_y = laser_route[-1] # 마지막
        grid[last_x][last_y] -= attack
        laser_route = laser_route[:-1]
        for laser in laser_route:
            x, y = laser
            half_attack = attack // 2 
            grid[x][y] -= half_attack
        damage_memo += laser_route

def simulate():

    global damage_memo, attack_memo, grid
    _, _, row_col, col = select_attacker()
    row = -(row_col - col)
    _, _, o_row_col, o_col = select_high(row, -col)
    row_o = -(o_row_col -o_col)
    col_o = -o_col

    if row >= 9999 or -col >= 9999:
        return
    if row_o >= 9999 or col_o <= -9999:
        return 
    
    grid[row][-col] += (n+m)
    damage_memo.append((row, -col))
    attack_memo[row][-col] +=1 # 공격한 거 표시 (숫자가 클 수록 최근에 공격자로 간택)

    laser_attack(row, -col, row_o, col_o)
    damage_memo.append((row_o, col_o))

    # 공격받고 포탑 부서짐
    for i in range(n):
        for j in range(m):
            if grid[i][j] <= 0:
                grid[i][j] = 0
    # 포탑 정비
    for i in range(n):
        for j in range(m):
            if (i,j) not in damage_memo and grid[i][j] != 0:
                # 공격과 무관한 
                grid[i][j] +=1

for _ in range(k):  
    damage_memo = []
    simulate()

ans = 0

for i in range(n):
    for j in range(m):
        if ans < grid[i][j]:
            ans = grid[i][j]
print("============")
print(ans)


