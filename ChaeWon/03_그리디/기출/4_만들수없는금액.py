'''
이코테 314p 
n개의 동전으로 만들 수 없는 양의 정수 금액 중 최솟값?
input 
5
3 2 1 1 9
output
8

'''

n = int(input())
coins = list(map(int,input().split()))
coins.sort()

able = 1

for c in coins:
  if able < c:
    break
  able += c
  
print(able)


