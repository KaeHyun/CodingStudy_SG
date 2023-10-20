# 2021 상반기 오전 1번 문제 (골드5) -- simulation

N = int(input())
like_friend = {} # 좋아하는 친구 딕셔너리 

ride_map = [[0]*(N+1) for _ in range(N+1)] # 놀이기구 격자 

for _ in range(N*N):
    n0, n1, n2, n3, n4 = map(int, input().split())
    like_friend[n0] = [n1, n2, n3, n4] # 딕셔너리에 값 추가

def in_range(x, y):
    if 1 <= x and x <= N and 1 <=y and y <= N:
        return True
    else:
        return False

def find_cell(n0_like, ride_map, i, j):
    # 좋아하는 친구가 주변에 몇 명 있는지
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    friend_cnt = 0
    blank_cnt = 0

    for idx in range(len(dx)):
        nx = i + dx[idx]
        ny = j + dy[idx]
        if in_range(nx, ny) and ride_map[nx][ny] in n0_like:
            # 해당 격자를 기준으로 한 칸 움직인 좌표가 범위 내에 해당하고 좋아하는 친구라면, friend_cnt 증가! 
            friend_cnt+=1
        elif in_range(nx, ny) and ride_map[nx][ny] == 0:
            # 해당 격자가 범위 안이고, 빈칸인 경우
            blank_cnt+=1

    return (friend_cnt, blank_cnt, -i, -j)

def take_ride(n0):
    # 우선순위 : 좋아하는 친구 수 > 빈칸 수 > 행의 번호가 작은 것 > 열의 번호가 작은 것
    # 행과 열로 우선순위가 떨어지면 큰게 아니라 작은 것을 골라줘야 한다. 따라서 "-" 로 변환해주자
    priority = (0, 0, -(N+1), -(N+1)) # 초기화도 행/열은 가장 작아야 비교 가능하므로 다음과 같이 초기화

    n0_like = like_friend[n0]
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            if ride_map[i][j] == 0: # 해당 칸이 비어있다면,
                candidate_cell = find_cell(n0_like, ride_map, i, j)
                if priority < candidate_cell:
                    # 후보 칸이 우선순위보다 더 좋으면
                    priority = candidate_cell

    _, _, r, c = priority
    ride_map[-r][-c] = n0 # 당사자 탑승
     
def make_score(like_friend, ride_map):

    friend_list = []
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(1,N+1):
        for j in range(1, N+1):
            friend_cnt = 0
            me = ride_map[i][j]
            my_friend = like_friend[me]
            for idx in range(4):
                nx = i + dx[idx]
                ny = j + dy[idx]
                if in_range(nx, ny) and ride_map[nx][ny] in my_friend:
                    friend_cnt +=1
            friend_list.append(friend_cnt)
    return friend_list


for i in enumerate(like_friend):
    idx, n0 = i
    take_ride(n0)

score_board = make_score(like_friend, ride_map)

ans = 0
for idx in score_board:
    if idx == 1: 
        ans +=1
    elif idx == 2:
        ans +=10
    elif idx == 3:
        ans +=100
    elif idx == 4:
        ans +=1000

print(ans)