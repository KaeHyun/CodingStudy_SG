# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    print(A)
    A= sorted(A)
    print(A)
    for i in range(2,len(A)):
        if (A[i-2] + A[i-1]) > A[i]:
            return 1
        else:
            return 0 
        
solution([10, 2, 5, 1, 8, 20])