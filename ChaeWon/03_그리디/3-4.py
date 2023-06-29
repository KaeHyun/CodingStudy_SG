# 예제 3-4 : 1이 될 때까지
'''
N이 1이 될 때까지 둘 중 하나를 반복해 선택 : n -= 1  , n/k (나눠떨어질때만).
결과값은 최소 실행 횟수
input 25 3
output 6

'''
n, k = map(int,input().split())
result = 0
temp = n
while True:
  if temp == 1:
    break
  if temp % k == 0:
    temp = temp // k
  else:
    temp -= 1
  result += 1

print(result)
