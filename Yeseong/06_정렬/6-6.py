array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

cnt = [0] * (max(array) + 1)

for i in range(len(array)):
    cnt[array[i]] += 1
# print(cnt)

for i in range(len(cnt)):
    for j in range(cnt[i]):
        print(i, end = ' ')