def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2 # 중간점이 실수일 때 소수점 버림
    
    if array[mid] == target:
        return mid + 1
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

print("전체 원소를 띄어쓰기 한 칸으로 구분하여 입력하세요.")    
array = list(map(int, input().split()))
n = len(array)
print("찾고자 하는 원소를 입력하세요.")
target = int(input())

result = binary_search(array, target, 0, n - 1)
if result is None:
    print("원소 {}을(를) 찾을 수 없습니다.".format(target))
else:
    print("원소 {}은(는) {}번 째 위치에 있습니다.".format(target, result))