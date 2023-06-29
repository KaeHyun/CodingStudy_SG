# 게임 개발

# 문제 요약 : 맵의 각 칸은 (A, B)인데, A칸은 북쪽으로부터 얼만큼 떨어졌고 B는 서쪽으로부터 얼만큼 떨어졌는지 / 바다로 되어 있는 공간은 갈 수 없음
#            1) 현재 위치에서 현재 방항야르 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다
#            2) 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전하고 왼쪽으로 한 칸 전진 / 왼쪽에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전 수행하고 1단계로 돌아감
#            3) 만약 네 방향 모두 이미 가본 칸 혹은 바다로 되어있다면, 바라보는 방향을 유지하고 한 칸 뒤로 가고 1단계로 돌아간다. 이때, 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없다면   움직임 멈춤
#            0: 육지 1: 바다

# 4 4
# 1 1 0
# 1 1 1 1 
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

n, m = map(int, input().split()) #맵의 세로크기 , 가로크기
y, x, d = map(int, input().split())

map_array = []
visit_array = []

for i in range(n):
    map_array.append(list(map(int, input().split())))

# 방문 기록 메모할 리스트
for i in range(n):
    visit_array.append([0] *m)

visit_array[y][x] = 1


while True:
    if d==0: #북쪽을 바라보고 있다면
        if map_array[y][x-1] == 0 and visit_array[y][x-1] == 0: #서쪽
            # 육지이고 가본 적이 없다면,
            d = 3 
            x = x-1
            visit_array[y][x] =1
        elif map_array[y+1][x] == 0 and visit_array[y+1][x] == 0: #남쪽
            d = 2
            y = y+1
            visit_array[y][x] =1
        elif map_array[y][x+1] == 0 and visit_array[y][x+1] == 0: #동쪽
            d = 1
            x = x+1
            visit_array[y][x] =1
        else:
            break
    elif d == 1: # 동쪽을 바라보고 있다면
        if map_array[y-1][x] == 0 and visit_array[y-1][x] == 0: #북쪽
            d = 0
            y = y-1
            visit_array[y][x] =1
        elif map_array[y][x-1] == 0 and visit_array[y][x-1] == 0: #서쪽
            d = 3 
            x = x-1
            visit_array[y][x] =1
        elif map_array[y+1][x] == 0 and visit_array[y+1][x] == 0: #남쪽
            d = 2
            y = y+1
            visit_array[y][x] =1
        else:
            break
    elif d == 2: # 남쪽을 바라보고 있다면
        if map_array[y][x+1] == 0 and visit_array[y][x+1] == 0: #동쪽
            d = 1
            x = x+1
            visit_array[y][x] =1
        elif map_array[y-1][x] == 0 and visit_array[y-1][x] == 0: #북쪽
            d = 0
            y = y-1
            visit_array[y][x] =1
        elif map_array[y][x-1] == 0 and visit_array[y][x-1] == 0: #서쪽
            d = 3 
            x = x-1
            visit_array[y][x] =1
        else:
            break
    elif d == 3: # 서쪽을 바라보고 있다면
        if map_array[y+1][x] == 0 and visit_array[y+1][x] == 0: #남쪽
            d = 2
            y = y+1
            visit_array[y][x] =1
        elif map_array[y][x+1] == 0 and visit_array[y][x+1] == 0: #동쪽
            d = 1
            x = x+1
            visit_array[y][x] =1
        elif map_array[y-1][x] == 0 and visit_array[y-1][x] == 0: #북쪽
            d = 0
            y = y-1
            visit_array[y][x] =1
        else:
            break
    else:
        break

# 이중 리스트에서 1의 개수 세기
ones_count = sum(sublist.count(1) for sublist in visit_array)
print(ones_count)
