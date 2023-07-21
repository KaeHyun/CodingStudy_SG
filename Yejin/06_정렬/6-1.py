# 선택정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)-1):
    minimum = min(array[i+1:])
    idx = array.index(minimum)
    if array[i] > minimum:
        array[i], array[idx] = array[idx], array[i]

print(array)