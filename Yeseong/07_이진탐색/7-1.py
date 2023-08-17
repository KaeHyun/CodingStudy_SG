def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1
        
print("문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()
n = len(array)
print("찾을 문자열을 입력하세요.")
target = input()

print("{}은(는) {}번 째 위치에 있습니다.".format(target, sequential_search(n, target, array)))