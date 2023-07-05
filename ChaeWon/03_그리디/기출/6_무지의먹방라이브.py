'''
무지의 먹방라이브
https://school.programmers.co.kr/learn/courses/30/lessons/42891
'''

# 효율성 테스트 시간초과
# def solution(food_times, k):
#     answer = 0
#     curT = 0
#     i = 0
#     n = len(food_times)
#     if sum(food_times) <= k:
#         return -1
#     while i < k :
#         if food_times[curT] > 0:
#             food_times[curT] -= 1
#             i += 1
#         curT = (curT+1)%n
#     while food_times[curT] == 0:
#         curT = (curT+1)%n
#     answer = curT + 1
#     return answer

def solution(food_times, k):
    n = len(food_times)
    if sum(food_times) <= k:
        return -1
    
    # 각 음식 (음식 번호, 소요 시간) 로 저장
    food_info = [(i, t) for i, t in enumerate(food_times, 1)]
    # 소요 시간을 기준 오름차순 정렬
    food_info.sort(key=lambda x: x[1]) 
    # 이전 음식의 소요 시간
    pre_time = 0  
  
    for i, (food_num, time) in enumerate(food_info):
        # 이전 음식과의 소요 시간 차이
        diff = time - pre_time  
        # 현재 음식부터 마지막 음식까지의 총 소요 시간
        total_time = diff * (n - i)  
        
        if total_time <= k:
            k -= total_time
            pre_time = time
        else:
            # 음식 번호를 기준으로 오름차순 정렬
            sub_list = sorted(food_info[i:], key=lambda x: x[0])  
            answer = sub_list[k % (n - i)][0]
            break
    
    return answer
