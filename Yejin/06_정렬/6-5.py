array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return
    
    pivot = array[start]
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= pivot:
            left += 1
        while right > start and array[right] >= pivot:
            right -= 1
        if left > right:
            array[start], array[right] = array[right], array[start]
            break
        array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
        

quick_sort(array, 0, len(array)-1)
print(array)