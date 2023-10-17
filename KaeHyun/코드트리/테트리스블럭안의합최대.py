# 2017 상반기 오전 1번 문제 (골드4) -- simulation

import sys

input = sys.stdin.readline
N, M = map(int, input().split())

block_map= []
for _ in range(N):
    block_map.append(list(map(int, input().split())))

blocks = [
    [  [1, 1, 1, 1],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0] ],

     [ [1, 0, 0, 0],
       [1, 0, 0, 0],
       [1, 0, 0, 0],
       [1, 0, 0, 0] ],

     [ [1, 1, 0, 0],
       [1, 1, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0] ],

     [ [1, 0, 0, 0],
       [1, 0, 0, 0],
       [1, 1, 0, 0],
       [0, 0, 0, 0] ],

     [ [0, 1, 0, 0],
       [0, 1, 0, 0],
       [1, 1, 0, 0],
       [0, 0, 0, 0] ],

     [ [1, 1, 1, 0],
       [1, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0] ],

     [ [1, 1, 1, 0],
       [0, 0, 1, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0] ],

     [ [1, 1, 0, 0],
       [0, 1, 0, 0],
       [0, 1, 0, 0],
       [0, 0, 0, 0] ],

     [ [1, 1, 0, 0],
       [1, 0, 0, 0],
       [1, 0, 0, 0],
       [0, 0, 0, 0] ],

     [ [0, 0, 1, 0],
       [1, 1, 1, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0] ],

     [ [1, 0, 0, 0],
       [1, 1, 1, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0] ],

     [ [1, 0, 0, 0],
       [1, 1, 0, 0],
       [0, 1, 0, 0],
       [0, 0, 0, 0] ],

     [ [0, 1, 1, 0],
       [1, 1, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0] ],

     [ [1, 1, 0, 0],
       [0, 1, 1, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0] ],

     [ [0, 1, 0, 0],
       [1, 1, 0, 0],
       [1, 0, 0, 0],
       [0, 0, 0, 0] ],

     [ [1, 0, 0, 0],
       [1, 1, 0, 0],
       [1, 0, 0, 0],
       [0, 0, 0, 0] ],

     [ [1, 1, 1, 0],
       [0, 1, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0] ],

     [ [0, 1, 0, 0],
       [1, 1, 0, 0],
       [0, 1, 0, 0],
       [0, 0, 0, 0] ],

     [ [0, 1, 0, 0],
       [1, 1, 1, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0] ]   
]

def in_range(x, y):
    if x >=0 and x < N and y >= 0 and y < M:
        return True
    else:
        return False

def make_score(x, y):
    max_score = 0
    for shape in blocks:
        tmp_score = 0
        # 블록의 모양 4 x 4 탐색 
        for i in range(4):
            for j in range(4):
                nx = x + i
                ny = y + j
                if in_range(nx, ny) and shape[i][j] == 1:
                    tmp_score += block_map[nx][ny]
        max_score = max(tmp_score, max_score)
    
    return max_score
max_ans=0
for i in range(N):
    for j in range(M):
        curr_score = make_score(i, j)
        if curr_score > max_ans:
            max_ans = curr_score
print(max_ans)


# 주어진 위치에 대하여 가능한 모든 모양을 탐색하며 최대 합을 반환합니다.
# def get_max_sum(x, y):
#     max_sum = 0
#     for shape in blocks:
#         sum_of_nums = sum([
#             block_map[x + dx][y + dy]
#             for dx in range(4)
#             for dy in range(4)
#             if in_range(x + dx, y + dy) and shape[dx][dy]
#         ])
#         max_sum = max(max_sum, sum_of_nums)
    
#     return max_sum


# # 격자의 각 위치에 대하여 탐색해줍니다.
# max_sum = max([
#     get_max_sum(i, j)
#     for i in range(N)
#     for j in range(M)
# ]) 
