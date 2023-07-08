# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # Implement your solution here
    answer = [0] *N
    max_counter = N +1
    temp = 0
    curr_max = 0

    for i in A:
        if i < max_counter: #그냥 더하기
            if answer[i-1] < temp:
                #만약 max counter 발생 후에 temp에 저장된 값보다 작다면
                #max counter 발생 전에 최대값보다 작았다.
                answer[i-1] = temp +1
            else:
                answer[i-1] += 1
            if answer[i-1] > curr_max:
                #계속해서 현재 최대값 update
                curr_max = answer[i-1]
        else:
            # Max counter 발생!
            temp = curr_max #temp 변수에 현재 max_val 값을 저장 
        
    for idx in range(N):
        if answer[idx] < temp:
            answer[idx] =temp
    
    return answer

solution (5, [3, 4, 4, 6, 1, 4, 4])