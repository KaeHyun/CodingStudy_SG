n, k = map(int, input().split())
res = 0

while n != 1:
    if n % k == 0:
        n /= k
    else:
        n -= 1
    res += 1

print(res)