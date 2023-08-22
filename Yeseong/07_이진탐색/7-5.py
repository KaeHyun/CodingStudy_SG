def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
array = sorted(list(map(int, input().split())))

m = int(input())
request = list(map(int, input().split()))

for i in request:
    result = binary_search(array, i, 0, n - 1)
    if result == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')