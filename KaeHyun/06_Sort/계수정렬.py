# 계수정렬 -> 일반적으로 별도의 리스트를 선언하고 그 안에 정렬에 대한 정보를 담는다
# 시간복잡도 : O(n+k) n = 데이터의 개수, k = 데이터의 최댓값


array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

max_num = max(array)
min_num = min(array)
length = (max_num - min_num) +1

sort_list = [ 0 for _ in range(length)]
#print(sort_list)

for i in range(len(array)):
    sort_list[array[i]] += 1

for i in range(len(sort_list)):
    for j in range(sort_list[i]): 
        print(i, end=' ')