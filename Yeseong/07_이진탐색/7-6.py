# 계수정렬 이용한 방법
n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
request = list(map(int, input().split()))

for i in request:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')