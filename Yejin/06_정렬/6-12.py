# 두 배열의 원소 교체
n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

for i in range(k):
    if a[i] >= b[len(b)-i-1]:
        break
    a[i] = b[len(b)-i-1]

print(sum(a))