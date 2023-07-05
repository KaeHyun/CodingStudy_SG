'''
A,B 두사람이 서로 무게가 다른 볼링공을 고름
볼링공 총 n개, 최대 무게 m, 각각 무게 입력받음
같은 무게 공도 다르게 봄
둘이 볼링공 고르는 경우의 수 ?
input
5 3
1 3 2 3 2
output
8
input
8 5
1 5 4 3 2 4 5 2
output
25
'''

n,m = map(int,input().split())
balls = list(map(int,input().split()))
result = 0

for i in range(len(balls)-1):
  for j in range(i+1,len(balls)):
    if balls[i] != balls[j]:
      result += 1
print(result)
