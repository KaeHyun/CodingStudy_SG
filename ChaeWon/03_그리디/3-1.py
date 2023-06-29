# 예제 3-1 거스름돈 : 500, 100, 50, 10 으로 최소개수로 N원 거슬러주기

n = int(input())
coins = [500,100,50,10]
result = 0
temp = n
for c in coins:
  result += temp //c
  temp = temp % c
print(result)

