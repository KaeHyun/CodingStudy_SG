# 퀵 정렬
# 시간복잡도: O(nlogn)
#  주의사항: 이미 정렬된 데이터일 경우 최악의 O(n^2) 시간복잡도를 가질 수도 있다.

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def qsort(array):
    if len(array) <=1: #리스트의 길이가 1보다 작거나 같으면 그냥 return 
        return array
    
    pivot= array[0]
    new_array = array[1:] # pivot 제외

    left = [x for x in new_array if x <= pivot]
    right = [x for x in new_array if x > pivot]
    

    return qsort(left) + [pivot] + qsort(right) 


print(qsort(array))
