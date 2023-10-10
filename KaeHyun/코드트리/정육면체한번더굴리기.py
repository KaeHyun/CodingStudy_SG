# 2021 하반기 오전 1번 문제 (골드3)
import sys
from collections import deque

input = sys.stdin.readline
# n= 격자의 크기, m= 굴리는 횟수
n, m = map(int, input().split())
grid_map = []
for _ in range(n):
    grid_map.append(list(map(int, input().split())))

# 주사위는 항상 초기에 격자판의 1행 1열에 놓여져 있고, 처음에는 항상 오른쪽으로 움직임
# 0: 위, 1: 오른쪽, 2: 아래, 3: 왼쪽
directions = 1 # 초기 방향
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
dice = [1, 2, 3] # up, front, side
queue = deque()

def in_range(x, y):
    if x>=0 and x < n and y>=0 and y<n:
        return True
    else:
        return False

def dice_dir(x, y, dice, grid_map, dir):
    curr_grid = grid_map[x][y]
    curr_dice = 7 - dice[0] # 7 - 위를 보고 있는 숫자
    if curr_grid > curr_dice:
        # 반시계 방향으로 진행방향 90도 회전
        if dir == 0:
            dir = 3
        else:
            dir -=1
    elif curr_grid < curr_dice:
        # 시계 방향으로 진행방향 90도 회전
        if dir == 3:
            dir = 0
        else:
            dir +=1
    # 만약 같다면 그냥 dir 유지 
    return dir

def move_dice(x, y, dice, dir):
    nx = x + dx[dir]
    ny = y + dy[dir]
    if in_range(nx, ny): # 격자 안에 존재한다면 
        if dir == 0:
            tmp_up = dice[0]
            dice[0] = dice[1]
            dice[1] = 7 - tmp_up
        elif dir == 1:
            tmp_side = dice[2]
            dice[2] = dice[0]
            dice[0] = 7 - tmp_side
        elif dir == 2:
            tmp_front = dice[1]
            dice[1] = dice[0]
            dice[0] = 7 - tmp_front
        elif dir == 3:
            tmp_up = dice[0]
            dice[0] = dice[2]
            dice[2] = 7 - tmp_up
        return nx, ny, dice, dir     
    else:
        # 격자 안에 없다면 방향 정 반대로 바꿔주기
        if dir >= 2:
            dir -=2
        else:
            dir +=2
        nx = x + dx[dir]
        ny = y + dy[dir]
        if dir == 0:
            tmp_up = dice[0]
            dice[0] = dice[1]
            dice[1] = 7 - tmp_up
        elif dir == 1:
            tmp_side = dice[2]
            dice[2] = dice[0]
            dice[0] = 7 - tmp_side
        elif dir == 2:
            tmp_front = dice[1]
            dice[1] = dice[0]
            dice[0] = 7 - tmp_front
        elif dir == 3:
            tmp_up = dice[0]
            dice[0] = dice[2]
            dice[2] = 7 - tmp_up
        return nx, ny, dice, dir   



def make_score(x, y, grid_map): # BFS?
    visit_map= [[0]*n for _ in range(n)]
    curr_num = grid_map[x][y] # 현재 주사위가 올라가있는 판의 숫자 저장
    visit_map[x][y] = -1
    queue.append((x,y))
    count = 0
    while queue:
        x, y = queue.popleft()
        count +=1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if in_range(nx, ny) and grid_map[nx][ny] == curr_num and visit_map[nx][ny] == 0:
                queue.append((nx,ny))
                visit_map[nx][ny] = 1
    score = curr_num * count

    
    return score

score = 0
# 가장 처음은 for문 없이 진행
x, y = 0,0
x, y, dice, directions = move_dice(x, y, dice, directions)
#print(x, y, dice, directions)
score = make_score(x, y, grid_map)


for i in range(1, m):
    directions = dice_dir(x, y, dice, grid_map, directions)
    x, y, dice, directions = move_dice(x, y, dice, directions)
    score += make_score(x, y, grid_map)

print(score)