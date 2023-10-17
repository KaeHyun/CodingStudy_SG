# 2020 상반기 오전 1번 문제 (골드5)
import sys
from collections import deque

input = sys.stdin.readline
# n = 무빙워크의 길이 / k = 실험을 종료할 0 의 개수 
n, k = map(int, input().split())
limit = n*2 # 무빙워크의 최대 길이
move_walk = [] #회전할 무빙워크
for i in range(1, n*2+1):
    move_walk.append(i)
stability = list(map(int, input().split())) # 무빙워크의 안정성 정보
people_list = [0]*limit # 사람이 무빙워크 어디에 탔는지에대한 정보
people_info = deque()

def rotate_move_walk(move_walk): # 무빙워크 회전 함수
    tmp = [0]*limit
    for i in range(len(move_walk)):
        idx = i+1
        if idx == limit:
            # 가장 끝에 있는 무빙워크
            idx = 0
        tmp[idx] = move_walk[i]
    move_walk = tmp

    return move_walk

ans = 1 # 실험 횟수 (초기에 1로 두자)

def do_experiment(move_walk, people_list, people_info, stability, ans):
    # 1. 무빙워크가 한 칸 회전 (무빙워크에 탄 사람 정보도 회전)
    move_walk = rotate_move_walk(move_walk)
    people_list = rotate_move_walk(people_list)
    stability = rotate_move_walk(stability)
    
    if len(people_info) != 0:
        for idx in range(len(people_info)):
            if people_info[idx] == limit:
                people_info[idx] = 0
            else:
                people_info[idx] +=1
   
    # 2. 가장 먼저 무빙워크에 올라온 사람부터 무빙워크가 회전하는 방향으로 한 칸 이동할 수 있으면 이동
    for _ in range(len(people_info)):
        # n 번째 칸에 도착하면 사람 제거
        idx = people_info.popleft()
        if idx >= (n-1):
            people_list[idx] = 0
        # 다음칸에 사람 없고, 안정성 0이 아니라면, 
        elif people_list[idx+1] == 0 and stability[idx+1] != 0 and idx != n:
            people_list[idx+1] = 1
            people_list[idx] = 0
            stability[idx+1] -= 1
            people_info.append(idx+1)
        else:
            people_info.append(idx)

    # 3. 1번 칸에 사람 없고, 안정성이 0이 아니라면 사람 한 명 더 올림
    if stability[0] != 0 and people_list[0] != 1:
        stability[0] -= 1
        people_list[0] = 1
        people_info.append(0)

    # 4. 안정이 0인 칸이 k개 이상이라면, 과정 종료 
    cnt = stability.count(0)
    if cnt >= k:
        return ans
    else:
        ans += 1

print(do_experiment())

