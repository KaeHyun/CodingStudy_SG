'''
이코테 311p (그리디 기출) 01 모험가 길드
n명의 모험가들, 각각 공포도 x
공포도가 x인 모험가는 반드시 x명 이상으로 구성한 모험가 그룹에 참여해야
여행을 떠날 수 있음. 
최대 몇개의 모험가 그룹을 만들 수 있을까?
input
5
2 3 1 2 2 
output
2
'''

n = int(input())
data = list(map(int,input().split()))
data.sort()
result = 0
i = 0
while i < n:
  cur = data[i]
  if cur < n and data[i+cur-1] <= cur:
    result += 1
    i += cur
  else:
    break
print(result)
    
    
