# 치킨배달
# 백준 15686 골드 5
# https://www.acmicpc.net/problem/15686
# 조합을 사용해보자!

import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
city = []
home = []
home_len = []
chicken = []

for i in range(n):
    city.append(list(map(int, input().split())))

# 집, 치킨 위치 저장
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

all_combi = combinations(chicken, m)

# 치킨 거리 구하기
for combi in all_combi:
    sum_len = 0
    for a, b in home:
        length = 1000
        for x, y in combi:
            cur_len = abs(x-a) + abs(y-b)
            if length > cur_len:
                length = cur_len
        sum_len += length
    home_len.append(sum_len)

print(min(home_len))