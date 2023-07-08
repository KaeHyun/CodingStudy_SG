# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# def solution(A):
#     # Implement your solution here
#     if len(A) < 2:
#         #길이가 0 또는 1이라면 그냥 1
#         return 0 
#     minIdx = A.index(min(A)) #최소값이 저장되어있는 index 찾기
#     #print(maxIdx)
#     profit =0 
#     tmp = 0 
#     for i in range(minIdx+1, len(A)):
#         profit = A[i] - A[minIdx]
#         if profit > tmp :
#             tmp = profit
#     #print(profit)
#     return profit 


def solution(A):
    # Implement your solution here
    if len(A) < 2:
        #길이가 0 또는 1이라면 그냥 1 return
        return 0 
    #minIdx = A.index(min(A)) #최소값이 저장되어있는 index 찾기
    #print(maxIdx)
    maxVal=0
    minVal = A[0]
    for i in range(1, len(A)):
        if minVal > A[i]:
            minVal = A[i] 
        profit = A[i] - minVal
        if profit > maxVal :
            maxVal = profit
    return maxVal

solution([23171, 21011, 21123, 21366, 21013, 21367])
#return 값이 356