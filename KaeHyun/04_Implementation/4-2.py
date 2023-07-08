# 시각

# 문제 요약 : 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지 3이 하나라도 포함되는 모든 경우를 구하는 프로그램

N = int(input())

count = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            # 13 23 과 같은 경우도 커버하기 위해서는 문자열로 변환해서 생각
            if '3' in str(i) + str(j) + str(k):
                count +=1
print(count)