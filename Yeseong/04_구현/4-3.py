cur = input()

row = int(cur[1])
col = int(ord(cur[0])) - int(ord('a')) + 1 # 문자 형태의 열을 1~8의 숫자로 변환

steps = [(-2,-1), (-1,-2), (-2,1), (-1,2), (2,-1), (1,-2), (2,1), (1,2)]

cnt = 0
for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        cnt += 1
        
print(cnt)