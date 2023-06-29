# https://www.acmicpc.net/problem/2839

n = int(input())
'''
봉지는 3, 5 kg 
5를 최대로 사용한 경우부터 그 나머지를 3의 배수로 채워나가는 걸 비교
'''

result = 9999
temp = n
if temp % 5 == 0:
  result = temp // 5
else:
  count = temp // 5
  for i in range(count,-1,-1):
    if (temp - 5*i)%3 == 0:
      result = min(result,i + (temp - 5*i)//3 )
  if result == 9999:
    result = -1
print(result)

