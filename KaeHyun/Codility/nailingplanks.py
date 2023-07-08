# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

#실패 ####


def solution(A, B, C):
    # Implement your solution here
    start = 0 
    end = len(C) - 1
    N = len(A)
    C= sorted(C)
    nailed = [0] *N
    answer = [] 
    while start <= end : 
        mid = (start + end) //2
        idx = 0
        for i in range(len(A)):
            if A[i] <= C[mid] and B[i] >= C[mid] and nailed[i] == 0:
                #나사를 박을 수 있으면
                nailed[i] = 1 #nailed 표시
                idx = i 
                answer.append(C[mid])
        if idx >= (N//2):
            start = start +1
        else:
            end = end-1
    answer = set(answer)
    print(len(answer))
    return len(answer)      
            

solution([1, 4, 5, 8], [4, 5, 9, 10], [4, 6, 7, 10, 2])


#랜선자르기 -이분탐색

# count = []

# K, N = map(int, input().split())

# #리스트에 저장 
# for _ in range(K):
#     count.append(int(input()))

# start = 1
# end = max(count)


# while start <= end : 
#     mid = (start + end) //2
#     #print("middle: " + str(mid))
#     sum = 0

#     for i in range(0,K):
#         sum += (count[i]//mid)
#     #print("sum: " + str(sum))

#     if sum >= N:
#          #원하는 값보다 sum의 크기가 더 작다 ,, 즉 랜선을 나누려는 길이가 더 길어져야겠지?
#         start = mid +1
#     else:
#         #원하는 값이 sum의 크기보다 크다 ,, 즉 랜선을 나누려는 길이가 짧아져야겠지?
#         end = mid -1

# #최대 랜선 길이이기 때문에 
# print(end)





    