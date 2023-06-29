'''
이코테 118p
3 실전 문제 : 게임 개발 
N*M 크기의 직사각형. 각 칸은 육지 or 바다. 캐릭터는 4방향 중 1을 바라봄
A는 북쪽으로부터 떨어진 개수 B는 서쪽으로부터 떨어진 개수. 바다는 못감
0 1 2 3 북동남서 방향 U R D L
0 : 육지 1 : 바다

캐릭터 이동 메뉴얼
1.현재방향 기준 왼쪽부터 갈 곳을 정함
2.캐릭터 바로 왼쪽에 가보지않은 칸이 존재 시 왼쪽 방향으로 회전 후 왼쪽으로 한칸 전진. 없으면 회전만하고 1단계로
3.네 방향 모두 이미 가봤든지 바다면. 바라보는 방향 유지한 채 한칸 뒤로가고 1단계로. 이때 뒤가 바다면 움직임을 멈춤

메뉴얼에 따라 캐릭터를 이동시킨 다음 캐릭터가 방문한 칸 수를 출력해라

input
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
output
3
'''
n, m = map(int,input().split())
cur_x, cur_y, dir = map(int,input().split())
result = 0
data = []
for _ in range(n):
  data.append(list(map(int,input().split())))
dx = [-1,0,1,0] # 북동남서
dy = [0,1,0,-1]
visited = [[0]*m for _ in range(n)]
visited[cur_x][cur_y] = 1
cur_dir = dir
count = 0

while True:
  moved = 0
  for _ in range(4):
    cur_dir -= 1
    if cur_dir == -1:
      cur_dir = 3
    nx = cur_x + dx[cur_dir]
    ny = cur_y + dy[cur_dir]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
      continue
    if visited[nx][ny] == 0 and data[nx][ny] == 0:
      visited[nx][ny] = 1
      cur_x, cur_y = nx, ny
      moved = 1
      break
  if moved == 0 :
    nx = cur_x - dx[cur_dir]
    ny = cur_y - dy[cur_dir]
    if data[nx][ny] == 1 or nx < 0 or nx >= n or ny < 0 or ny >= m:
      break
    cur_x, cur_y = nx, ny
    
print(sum([ sum(v) for v in visited]))
  
  
    
    
    
