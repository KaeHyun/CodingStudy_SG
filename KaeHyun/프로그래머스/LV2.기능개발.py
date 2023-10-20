from collections import deque

def check(queue, day):
    count = 0 

    for q in queue:
        if q <= day:
            count +=1
        else:
            return count
    return count

def solution(progresses, speeds):
    answer = []
    days = [] # 배포까지 필요한 일 수 
    
    for i in range(len(progresses)):
        # 남은 작업 진도로 전부 대체 
        progresses[i] = 100 - progresses[i]
        if progresses[i] % speeds[i] != 0:
            days.append(int(progresses[i]/speeds[i])+1)
        else:
            days.append(int(progresses[i]/speeds[i]))

    dayq = deque(days)

    while dayq:
        day = dayq.popleft() 
        tmp_count = check(dayq, day)
        for _ in range(tmp_count):
            dayq.popleft()
        answer.append(tmp_count+1)
    
    return answer

solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])