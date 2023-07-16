# 삽입 정렬

# 삽입 정렬의 시각복잡도는? O(n^2)
# 삽입 정렬의 포인트: 현재 리스트의 data가 거의 정렬되어 있다면, 매우 빠르게 동작한다

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
print(array)