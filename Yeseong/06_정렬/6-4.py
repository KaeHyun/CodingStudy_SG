array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개 남은 경우 퀵 정렬 종료
        return
    p = start
    left = start + 1
    right = end
    
    while left <= right:
        while left <= end and array[left] <= array[p]:
            left += 1
        while right > start and array[right] >= array[p]:
            right -= 1
        if left > right: # 왼쪽에서 찾은 값과 오른쪽에서 찾은 값이 엇갈린 경우
            array[right], array[p] = array[p],  array[right]
        else:
            array[left], array[right] = array[right],  array[left]
        
    quick_sort(array, start, right - 1) # 분할 이후 왼쪽 리스트에서 퀵 정렬 재귀적으로 수행
    quick_sort(array, right + 1, end) # 분할 이후 오른쪽 리스트에서 퀵 정렬 재귀적으로 수행

quick_sort(array, 0, len(array) - 1)
print(array)