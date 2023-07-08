# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(K, A):
    sum = 0
    count = 0
    for i in range(0, len(A)):
        sum += A[i]
        if sum >= K :
            count +=1
            sum =0 
    
    #print(count)
    return count



solution(4, [1, 2, 3, 4, 1, 1, 3])