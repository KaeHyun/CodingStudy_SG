'''
2 실전 문제 : 왕실의 나이트
8*8 왕실 정원 특정한 칸에 나이트
위치가 주어졌을 때 갈 수 있는 경우의 수 구하기
행 1~8 ,열 a~h
input : c2 / output : 6
'''
now = list(input()) # now[0] 열 now[1] 행
now[0] = str(ord(now[0])-96)
now = list(map(int,now))
dx = [2,2,-2,-2,1,1,-1,-1]
dy = [1,-1,1,-1,2,-2,2,-2]
result = 0
for i in range(8):
  nx = now[1] + dx[i]
  ny = now[0] + dy[i]
  if 1 <= nx <= 8 and 1 <= ny <= 8:
    result += 1
print(result)

