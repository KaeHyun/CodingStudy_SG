n, m = map(int, input().split())
res = []

for i in range(n):
    res.append(min(map(int, input().split())))

print(max(res))