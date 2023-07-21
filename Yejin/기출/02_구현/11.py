# 백준 3190 골드4
# 뱀
from collections import deque
import sys

input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n = int(input())
k = int(input())
board = [[0] * n for _ in range(n)]
snake = [[0] * n for _ in range(n)]
rotate = [""] * 10000
time = 1
rotation = 0
x = 0
y = 0
tail_deque = deque()
tail_deque.append((0, 0))
snake_len = 1

snake[0][0] = 1

for i in range(k):
    l, c = map(int, input().split())
    board[l-1][c-1] = 1

l = int(input())

for i in range(l):
    idx, c = map(str, input().split())
    rotate[int(idx)] = c

while k >= 0:
    # 방향
    if rotate[time-1]:
        if rotate[time-1] == 'D':
            rotation += 1
        else:
            rotation -= 1
    if rotation >= 4 :
        rotation -= 4
    if rotation < 0 :
        rotation += 4

    # 이동
    nx = x + dx[rotation]
    ny = y + dy[rotation]
    if(0<= nx < n and 0 <= ny < n):
        if(snake[ny][nx] == 1): # 자기 몸 부딪힘
            break
        if(board[ny][nx] == 1): # 사과 있음
            board[ny][nx] = 0
            snake[ny][nx] = 1
            tail_deque.append((ny, nx))
            k -= 1
            time += 1
            snake_len += 1
            x, y = nx, ny
        elif(board[ny][nx] == 0): # 사과 없음
            if snake_len > 1:
                ty, tx = tail_deque.popleft()
                snake[ty][tx] = 0
            else:
                snake[y][x] = 0
                tail_deque.popleft()
            tail_deque.append((ny, nx))
            snake[ny][nx] = 1
            time += 1
            x, y = nx, ny
    else: # 벽 부딪힘
        break

print(time)