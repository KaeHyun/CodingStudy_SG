# 떡볶이 떡 만들기
n, m = map(int, input().split())
dduck = list(map(int, input().split()))

dduck.sort()
start = 0
end = max(dduck)

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for i in dduck:
        if i - mid > 0:
            sum += i - mid
    
    if sum == m:
        print(mid)
        break
    elif sum < m:
        end = mid - 1
    else:
        start = mid + 1