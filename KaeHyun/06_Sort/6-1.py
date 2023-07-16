# 선택 정렬 알고리즘 : 가장 작은 값을 선택해서 맨 앞으로 보내는 방식

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    idx = i # 가장 앞에 있는 원소의 index

    for j in range(1, len(array)):
        if array[idx] > array[j]:
            idx = j
    tmp = array[i]
    array[i] = array[idx]
    array[idx] = tmp
    

print(array)
