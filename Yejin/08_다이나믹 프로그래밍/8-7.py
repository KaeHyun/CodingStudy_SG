# 바닥 공사
# 아니진짜 DP 넘 어려워요 흑흑

n = int(input())
dp = [0] * 1001

dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2] * 2) % 796796

print(dp[n])
