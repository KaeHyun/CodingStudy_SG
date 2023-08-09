# 효율적인 화폐 구성
# 답안 참고..

n, m = map(int, input().split())
array = []
dp = [10001] * 10000
dp[0] = 0

for i in range(n):
    array.append(int(input()))

for i in array:
    for j in range(i, m+1):
        if dp[j-i] != 10001:
            dp[j] = min(dp[j], dp[j-i]+1)

print(dp[m])