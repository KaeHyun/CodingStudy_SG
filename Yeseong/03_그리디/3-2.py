n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
first = nums[-1]
second = nums[-2]

# (first * k + second) 과정을 한 set로 가정 후 반복
result = (first * k + second) * (m // (k + 1))
result += first * (m % (k + 1)) # (m % (k + 1)) <= k 이므로 남은 더해지는 횟수동안 first를 더함 

print(result)