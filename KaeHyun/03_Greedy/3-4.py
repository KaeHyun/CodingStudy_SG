# 1이 될 때까지

# 문제 요약: 어떠한 수가 1이 될 때까지 다음의 두 과정 중 하나를 반복 수행
#           1. N에서 1을 뺀다
#           2. N을 K로 나눈다. (N이 K로 나누어 떨어질 때만 가능)

n, k = map(int, input().split())
count =0

while True:
    if n != 1:
        if n % k ==0:
            n /= k
            count +=1
        else:
            n -=1
            count +=1
    else:
        break

print(count)

