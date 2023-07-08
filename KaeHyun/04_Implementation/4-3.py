# 왕실의 나이트

# 문제 요약: 나이트의 초기 위치가 주어지면 이동할 수 있는 경우의 수를 출력 / 게임 판은 8x8로 열은 a ~ h 까지만 존재

start = list(str(input()))
col, row = ord(start[0]), start[1]

move_list = [(2, -1), (2, 1), (-2, -1), (-2, 1), (1, 2), (-1, 2), (1, -2) , (-1, -2)] #모든 경우의 수 8가지 

ans = 0

for i in move_list:
    tmp_col = col + i[0]
    tmp_row = int(row) + i[1]

    if tmp_col <= ord("h") and tmp_col >= ord("a") and tmp_row <= 8 and tmp_row >=1:
        ans +=1

print(ans) 


# 기억할 점 : 아스키 코드로 변형해서 문자열과 정수 계산 가능 "ord()"