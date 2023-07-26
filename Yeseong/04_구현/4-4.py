n, m = map(int, input().split())
x, y, direction = map(int, input().split())

# 북, 동, 남, 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

visit_check = [[0] * m for _ in range(n)] # 캐릭터가 방문한 칸 check하는 용도, 방문한 경우: 1
visit_check[x][y] = 1 # 처음 시작 칸은 방문처리

map_arr = []
for _ in range(n):
    map_arr.append(list(map(int, input().split())))


# 왼쪽 회전이 반복적으로 수행되므로 함수처리 / 북: 0, 동: 1, 남: 2, 서: 3
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3 # 0 ~ 3

visit_cnt = 1
turn_time = 0

while True:
    turn_left()
    next_x = x + dx[direction]
    next_y = y + dy[direction]
    
    if visit_check[next_x][next_y] == 0 and map_arr[next_x][next_y] == 0:
        visit_check[next_x][next_y] = 1
        x = next_x
        y = next_y
        visit_cnt += 1
        turn_time = 0
    else:
        turn_time += 1
        
        
    if turn_time == 4:
        next_x = x - dx[direction]
        next_y = y - dy[direction]
        if visit_check[next_x][next_y] == 0:
            x = next_x
            y = next_y
        else:
            break
        turn_time = 0
        
print(visit_cnt)
        
