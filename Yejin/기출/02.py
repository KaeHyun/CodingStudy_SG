s = input()
res = int(s[0])

for i in range(1, len(s)):
    if int(s[i-1]) <= 1: # 1일때도, 곱하는 것 보다 더하는 게 더 큼
        res += int(s[i])
    else:
        res *= int(s[i])

print(res)