# 위에서 아래로 -> 내림차순

N = int(input()) # 수열에 속해있는 수의 개수 

array = []

for i in range(N):
    array.append(int(input()))

array= sorted(array, reverse=True)

for i in array:
    print(i, end=" ")