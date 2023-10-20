# 3킬로그램 봉지와 5킬로그램 봉지
# 입력 : 18 출력: 4
N = int(input())

answer = 0

while N>0:
    if N % 5 == 0: # 나눈 값이 5로 나누어 떨어진다면, 
        answer += (N//5)
        N = 0
    else:
        # 5로 안 나누어 떨어진다면, 
        N -=3
        answer +=1
        if N < 0:
            answer = -1

print(answer)