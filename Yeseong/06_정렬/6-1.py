array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 이때 min()함수를 쓰면 선택정렬의 시간복잡도가 O(N^2) -> O(N^3)으로 증가함
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    
    array[i], array[min_index] = array[min_index], array[i] # 스와프 코드
    
print(array)