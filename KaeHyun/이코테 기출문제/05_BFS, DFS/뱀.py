# 백준 3190 번
# 문제요약: 뱀이 지나다니면서 사과 먹고 다 먹으면 게임 끝나고 아니면 자기 몸과 부딪히면 사망하는 게임 (물론 지도의 벽과도 부딪히면 안됨)
# 사과위치 : 1 / 뱀이 차지하는 위치 : 2

# 6  -> 보드의 크기 
# 3 -> 사과의 개수
# 3 4
# 2 5
# 5 3
# 3 ->뱀의 방향 전환
# 3 D : 오른쪽
# 15 L : 왼쪽
# 17 D
import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N = int(input())
M = int(input())

apple_map = [[0]*N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    apple_map[a-1][b-1] = 1

K = int(input())

info = []
for _ in range(K):
    info.append(list(input().split()))

x = 0 
y = 0

# return할 정답
time = 0
snake = deque()

while(1):
    #처음 움직일때, 오른 쪽 방향
    xt = x + dx[3]
    time +=1

    if apple_map[y][xt] == 1: #사과가 있다면
        snake.append((y,xt))
    
    
    

