# 2021 상반기 오전 2번 문제 (골드2)
from collections import deque
# n:  격자의 크기, m: 빨간색이 아닌 폭탄의 종류 
n, m = map(int, input().split())
bomb_map = []

RED = 0 
ROCK = -1
EMPTY = -2

ans = 0

for _ in range(n):
    bomb_map.append(list(map(int, input().split())))

temp_map = [[EMPTY] * n for _ in range(n)]

visitied = [[0]*n for _ in range(n)] # BFS 변수
queue = deque()

# 상 좌 하 우 
dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

def in_range(x, y):
    if x>=0 and x < n and y>=0 and y <n:
        return True
    else:
        return False

def BFS(x, y, color):
    
    # 초기화
    for i in range(n):
        for j in range(n):
            visitied[i][j] = 0 

    queue.append((x,y))
    visitied[x][y] =1 

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and visitied[nx][ny] != 1 and ( bomb_map[nx][ny] == color or bomb_map[nx][ny] == RED):
                # 격자 내에 존재하고 방문한 적 없고, 폭탄 색이 같거나 빨간 폭탄이면
                queue.append((nx, ny))
                visitied[nx][ny] = 1

def bomb_group(x, y):
    
    color = bomb_map[x][y]

    BFS(x, y, color) 

    # group 정보 계산
    bomb_count, red_count = 0, 0

    grid_stand = (-1, -1)

    for i in range(n):
        for j in range(n):
            if visitied[i][j] != 1:
                continue
            bomb_count +=1
            
            if bomb_map[i][j] == RED:
                red_count +=1
            elif (i, -j) > grid_stand:
                # 행은 클수록 열은 작을 수록 좋음
                grid_stand = (i, -j)
    
    row, col = grid_stand

    return ((bomb_count, -red_count, row, col))

def find_best_group():
    # 가장 크기가 큰 폭탄 묵음 찾기 ( BFS )

    best_group = (-1, -1, -1, -1) # 폭탄 그룹 크기, 빨간 폭탄 개수, 행 번호, 열 번호 

    for i in range(n):
        for j in range(n):
            bomb_color = bomb_map[i][j] # 폭탄의 색깔
            if bomb_color >= 1: 
                # 폭탄 묶음 시작 지점이 돌이나 빨간색 폭탄이 아니라면, 
                group = bomb_group(i,j)
                if group > best_group:
                    best_group  = group
    return best_group

def explode(): # 폭타 폭발!
    for i in range(n):
        for j in range(n):
            if visitied[i][j]:
                bomb_map[i][j] = EMPTY
def gravity():
    # 중력 작용을 구현 (중력은 행의 인덱스가 +1 증가)
     # 중력 작용을 쉽게 구현하기 위해
    # temp 배열을 활용

    for i in range(n):
        for j in range(n):
            temp_map[i][j] = EMPTY
    
    for j in range(n):
        # 아래에서 위로 올라오면서 해당 위치에 폭탄이 있는 경우에만 temp에 쌓아주기
        # 단, 돌이 있으면 그 위에부터 폭탄이 쌓이도록
        last_idx = n-1
        for i in range(n-1, -1, -1):
            if bomb_map[i][j] == EMPTY:
                continue
            if bomb_map[i][j] == ROCK:
                last_idx = i
            temp_map[last_idx][j] = bomb_map[i][j]
            last_idx -=1
    
    # 다시 배열을 옮겨준다. 
    for i in range(n):
        for j in range(n):
            bomb_map[i][j] = temp_map[i][j]

def rotate():
    # temp 배열을 활용

    for i in range(n):
        for j in range(n):
            temp_map[i][j] = EMPTY
    
    # 기존 격자들을 반시계 방향으로 90도 회전 결과를 temp에 저장
    for j in range(n-1, -1, -1):
        for i in range(n):
            temp_map[n-1-j][i] = bomb_map[i][j]
    
    # 다시 temp 배열 옮겨주기
    for i in range(n):
        for j in range(n):
            bomb_map[i][j] = temp_map[i][j]

def clean(x, y):
    # Step1. (x, y)를 시작으로 지워야할 폭탄 묶음을 표시합니다.
    BFS(x, y, bomb_map[x][y])

    # Step2. 폭탄들을 전부 지워줍니다.
    explode()

    # Step3. 중력이 작용합니다.
    gravity()

def simulate():
    global ans
    
    # Step1. 크기가 최대인 폭탄 묶음을 찾습니다.
    best_bundle = find_best_group()
    bomb_cnt, _, x, y = best_bundle

    # 만약 폭탄 묶음이 없다면, 종료합니다.
    if best_bundle == (-1, -1, -1, -1) or bomb_cnt <= 1:
        return False

    # Step2. 선택된 폭탄 묶음에 해당하는 폭탄들을 전부 제거 후
    #        중력이 작용합니다.
    ans += bomb_cnt * bomb_cnt
    clean(x, -y)

    # Step3. 반시계 방향으로 90' 만큼 회전합니다.
    rotate()

    # Step4. 중력이 작용합니다.
    gravity()

    return True

while True:
    keep_going = simulate()
    
    if not keep_going:
        break

print(ans)