# 2021 상반기 오후 1번 문제 (골드5) -- simulation(dx, dy skill)

import sys
input = sys.stdin.readline
# n: 격자의 크기, m: 리브로수를 키우는 총 년 수
n, m = map(int, input().split())
nutri_map = [[0]*n for _ in range(n)]
# 초기 영양제 위치 좌측 하단 4개!
nutri_map[n-1][0] = 1
nutri_map[n-1][1] = 1
nutri_map[n-2][0] = 1  
nutri_map[n-2][1] = 1

nutri_pos= [(n-2, 0),(n-2, 1), (n-1,0), (n-1,1)]
tree_map = []

direction = []

for _ in range(n):
    tree_map.append(list(map(int, input().split())))
# 특수 영양제의 d: 이동규칙( → ↗ ↑ ↖ ← ↙ ↓ ↘), p: 이동 칸 수
for _ in range(m):
    direction.append(tuple(map(int, input().split())))

dx = [0, -1, -1, -1, 0, 1, 1, 1]     
dy = [1, 1, 0, -1, -1, -1, 0, 1]

def in_range(x, y):
    #이 함수에서는 범위 밖으로 넘어가면 반대편으로 돌아온다!
    if x >=0 and x < n and y >=0 and y < n:
        return x, y
    else:
        if x < 0:
            x = n-1
        if x >= n:
            x = 0
        if y < 0:
            y = n-1
        if y >= n:
            y = 0
        return x, y
    
def move_nutri(nutri_map, nutri_pos, d, p):
    # 영양제를 주어진 방향에 따라 움직이기
    # 대각선까지 포함한 방향들! 
    dxx, dyy = dx[d-1], dy[d-1]
    for _ in range(p):
        for idx in range(len(nutri_pos)):
            pos = nutri_pos[idx]
            x, y = pos[0], pos[1]
            nx = x + dxx
            ny = y + dyy
            nx, ny = in_range(nx, ny)
            nutri_map[x][y] = 0
            nutri_pos[idx] = (nx, ny)
    # 좌표 다 옮기고 nutri_map update
    for pos in nutri_pos:
        x, y = pos[0], pos[1]
        nutri_map[x][y] =1
            
    return nutri_map, nutri_pos

def grow_tree(nutri_pos, tree_map):
    # 영양제 위치 정보 받아서 해당 땅의 나무 1 증가
    # 대각선에 높이 1 이상인 경우 나무 그만큼 +1
    for pos in nutri_pos:
        x, y = pos[0], pos[1]
        tree_map[x][y] +=1
    for pos in nutri_pos:
        x, y = pos[0], pos[1]
        if x-1>=0 and x-1 <n and y-1>=0 and y-1< n and tree_map[x-1][y-1] >=1:
            tree_map[x][y] +=1
        if x-1>=0 and x-1 <n and y+1 >=0 and y+1<n and tree_map[x-1][y+1] >=1:
            tree_map[x][y] +=1
        if x+1>=0 and x+1 < n and y-1>=0 and y-1< n and tree_map[x+1][y-1] >=1:
            tree_map[x][y] +=1
        if x+1>=0 and x+1 < n and y+1 >=0 and y+1<n and tree_map[x+1][y+1] >=1:
            tree_map[x][y] +=1
    return tree_map

def cut_and_relocate(nutri_map, nutri_pos, tree_map):
    # 특수 영양제 땅 제외: 높이가 2이상인 경우 2만큼 나무 길이 감소
    # 그리고 해당 땅에 영양제 위치하기
    new_nutri = []
    for i in range(n):
        for j in range(n):
            if tree_map[i][j] >=2 and nutri_map[i][j] != 1:
                # 나무의 높이가 2보다 크고 특수 영양제가 없는 땅이라면,
                tree_map[i][j] -=2 # 나무 길이 감소
                new_nutri.append((i,j)) # 새로운 영양제의 위치
    nutri_pos = new_nutri # 새로운 위치 원래 위치에다가 덮어쓰기
    nutri_map=[[0]*n for _ in range(n)] # 초기화
    
    for pos in nutri_pos:
        x, y = pos[0], pos[1]
        nutri_map[x][y] =1

    return nutri_map, nutri_pos, tree_map

for dir in direction:
    d, p = dir[0], dir[1]
    nutri_map, nutri_pos = move_nutri(nutri_map, nutri_pos, d, p)
    tree_map = grow_tree(nutri_pos, tree_map)
    nutri_map, nutri_pos, tree_map = cut_and_relocate(nutri_map, nutri_pos, tree_map)

ans = 0
for i in range(n):
    for j in range(n):
        ans +=tree_map[i][j]
print(ans)