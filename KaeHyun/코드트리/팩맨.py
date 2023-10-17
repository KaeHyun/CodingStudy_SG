#2021 하반기 오후 1번 문제 (골드1) 마무리!
from collections import deque
# m : 몬스터 수, t: 진행될 턴의 개수 
m, t = map(int, input().split())
# x, y: 팩맨의 초기 위치 
x, y = map(int, input().split())
# ↑,  ↖,  ←,  ↙,  ↓, ↘, →, ↗ 
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

x -=1
y -=1
monster_info = deque() # 몬스터의 위치 지도 (몬스터 위치 x, 몬스터 위치 y, 방향)
monster_map = [[0]*4 for _ in range(4)]
egg_map = [] # 몬스터의 알 (알의 존재여부, 방향)
dead_map = [[0] *4 for _ in range(4)] # 시체 위치 지도
dead_info = deque()
packman_map = [[0]*4 for _ in range(4)] # 팩맨의 위치
packman_map[x][y] = 1 


for _ in range(m):
    r, c, d = map(int, input().split())
    monster_info.append((r-1,c-1,d-1))
    monster_map[r-1][c-1] += 1

def in_range(x,y):
    return x >= 0 and x < 4 and y >=0 and y <4 

def copy_monster():
    # 매 턴마다 알은 부화하고 리셋 될 것 
    # 몬스터 복제 시도 : 현재 위치에서 자신과 같은 방향을 가진 몬스터 복제 -> 아직 알인 상태! 한 턴이 지나면 부화
    global monster_info, egg_map
    # 알 부화
    egg_map=[] # 매번 초기화
    egg_map = list(monster_info) # monster_info가 deque 라서 가능한 코드

def baby_monster():
    global monster_info, egg_map, monster_map
    # 알 부화
    for egg in egg_map:
        monster_info.append(egg)
        x, y, _ = egg
        monster_map[x][y] +=1

def check_move_monster(mx, my, md):

    cnt = 7
    new_d = md
    mnx, mny = mx + dx[md], my + dy[md]
    if in_range(mnx, mny) and dead_map[mnx][mny] == 0 and packman_map[mnx][mny] == 0:
        return mnx, mny, md 

    while (cnt != 0): # 8 방향 모두 확인
        new_d += 1
        if new_d > 7 :
             new_d = 0 
        mnx = mx + dx[new_d]
        mny = my + dy[new_d]
        if in_range(mnx, mny) and dead_map[mnx][mny] == 0 and packman_map[mnx][mny] == 0:
            # 격자 내에 존재하고 시체 없고 팩맨이 없다면 Return!
            return mnx, mny, new_d
        cnt -=1
    
    return mx, my, md 
        
        
def move_monster():
    # 몬스터 이동: 현재 자신이 가진 방향으로 1칸 이동
    # 시체 있거나 팩맨이 있거나 격자를 벗어나면 반시계 방향으로 45도 회전해서 갈 수 있는지 판단 
    # 만약 8 방향을 돌았는데도 못 움직이면 그대로 위치
    global monster_info, monster_map, dead_info

    new_info = deque()
    for mx, my, md in monster_info:
        mnx, mny, mnd = check_move_monster(mx, my, md)
        new_info.append((mnx, mny, mnd))
        monster_map[mx][my] -=1
        monster_map[mnx][mny] +=1

    # new_info를 바탕으로 새롭게 monster_map 업데이트
    monster_info = new_info

        
def eat_best(a, b, c):

    tmp_x, tmp_y = x, y
    eat_monster = 0
    dir = [a, b, c]
    visit_monster = [] # 방문 체크 

    for idx in dir:
        nx, ny = tmp_x + dx[idx], tmp_y + dy[idx]

        # 만약, 이동하다가 격자를 벗어나면 선택 X
        if not in_range(nx,ny):
            return -1, -1
        elif in_range(nx,ny) and (nx, ny) not in visit_monster:
            # 격자 안에 존재하고 
            eat_monster += monster_map[nx][ny]
            visit_monster.append((nx,ny))
        tmp_x, tmp_y = nx, ny 

    return eat_monster, dir

def move_packman():
    # 팩맨의 이동: 총 3칸 이동 / 대각선 움직이지 않음 / 몬스터를 가장 많이 먹을 수 있는 방향으로 이동
    # 우선순위: 상 - 좌 - 하 - 우
    # 몬스터를 먹으면 시체를 남긴다
    global packman_map, monster_map, monster_info, dead_info, x, y
    priority = [0, 2, 4, 6]
    food = -1
    best = deque([[-1, -1, -1]])
    for i in range(4):
        for j in range(4):
            for k in range(4):
                a, b, c = priority[i], priority[j], priority[k]
                tmp, ways = eat_best(a, b, c)
                if tmp == -1: # 격자 벗어나서 무시!
                    pass
                elif food < tmp:
                    food = tmp
                    best.append(ways)
                    best.popleft()
    # 팩맨의 위치 변경
    if best:
        best = best.popleft()
        for idx in best:
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if monster_map[nx][ny] != 0: # 몬스터가 해당 칸에 존재한다면!
                    # 몬스터 정보와 맵에서 몬스터 제거
                    monster_info = deque([mons for mons in monster_info if mons[:2] != (nx, ny)])
                    monster_map[nx][ny] = 0
                    # 몬스터를 먹으면 그 자리에 시체를 남긴다.
                    dead_info.append((nx, ny, 0))
                
                packman_map[x][y] = 0
                packman_map[nx][ny] = 1
                x, y = nx, ny
            
def delete_dead():
    # 몬스터의 시체는 2턴 유지
    global dead_info
    tmp_dead = deque()
    while dead_info:
        x, y, turn = dead_info.popleft()
        # 죽은 시체 정보에 따른 시체 배치 
        dead_map[x][y] =1
        turn +=1
        if turn > 2: 
            dead_map[x][y] =0
        else:
            tmp_dead.append((x,y, turn))

    dead_info = tmp_dead

for i in range(t):
    copy_monster()
    move_monster()
    move_packman()  # 이 함수 내에서 팩맨과 몬스터의 위치가 업데이트됩니다.
    delete_dead()
    baby_monster()

print(len(monster_info))

# 2 4
# 4 1
# 2 3 1
# 1 2 5