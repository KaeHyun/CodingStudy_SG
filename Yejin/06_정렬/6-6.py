# 계수 정렬
array = [0, 0, 1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9]
sorted_array = [0] * (max(array) + 1)

for i in array:
    sorted_array[i] += 1

for idx, value in enumerate(sorted_array):
    for i in range(value):
        print(idx, end=' ')