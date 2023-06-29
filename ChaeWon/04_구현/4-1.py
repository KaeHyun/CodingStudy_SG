# 04 구현
'''
예제 4-1 상하좌우 : 1,1 ~ N,N 
LRUD 로 움직여 도착지점 좌표 출력
input 
5
R R R U D D
output
3 4
'''
n = int(input())
data = list(input().split())
d = dict()
start = [1,1]
dx = [0,0,-1,1] # L R U D
dy = [-1,1,0,0]
for dir in data:
  if dir == "L" and 1 <= start[0]+dx[0] <= n and 1 <= start[1]+dy[0] <=n :
    start[0] += dx[0]
    start[1] += dy[0]
  if dir == "R" and 1 <= start[0]+dx[1] <= n and 1 <= start[1]+dy[1] <=n:
    start[0] += dx[1]
    start[1] += dy[1]
  if dir == "U" and 1 <= start[0]+dx[2] <= n and 1 <= start[1]+dy[2] <=n:
    start[0] += dx[2]
    start[1] += dy[2]
  if dir == "D" and 1 <= start[0]+dx[3] <= n and 1 <= start[1]+dy[3] <=n:
    start[0] += dx[3]
    start[1] += dy[3]
print(start[0],start[1])
