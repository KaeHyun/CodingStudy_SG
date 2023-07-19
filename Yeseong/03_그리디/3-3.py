n, m = map(int, input().split())

min_list = []

max_num = 0

for i in range(n):
    row = list(map(int, input().split()))
    min_num = min(row)
    max_num = max(max_num, min_num) # max_num이 매 row마다 update됨

print(max_num)
    