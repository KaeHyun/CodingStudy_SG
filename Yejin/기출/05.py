from itertools import permutations

n, m = map(int, input().split())
balls = list(map(int, input().split()))
res = 0
ab = list(permutations(balls, 2))

for (a, b) in ab:
    if a != b:
        res += 1

print(res//2)