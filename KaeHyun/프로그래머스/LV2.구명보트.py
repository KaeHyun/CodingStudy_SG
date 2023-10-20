# 구명보트 : 최대 2명, 무게 제한
# 포인트 : 제일 무거운 사람 + 제일 가벼운 사람 
from collections import deque

def solution(people, limit):
    count = 0
    
    queue = deque()
    people.sort(reverse=True)
    
    for i in people:
        queue.append(i)

    while queue:
        max_person = queue.popleft()
        min_person = min(people)
        if len(queue) == 0 :
            count +=1 
            break
        if max_person + min_person <= limit:
            count +=1
            queue.pop()
        else:
            count +=1
    print(count)        
    return count
  
        
solution([70, 80, 50, 50], 100)
solution([70, 80, 50], 100)