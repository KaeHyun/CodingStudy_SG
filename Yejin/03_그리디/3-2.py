n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

res = 0

while m > 0:
    for i in range(k):
        res += numbers[-1]
        m -=1
        if m == 0:
            break
    res += numbers[-2]
    m -= 1
    
print(res)