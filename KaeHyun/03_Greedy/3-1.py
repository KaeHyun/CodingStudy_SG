# 거스름돈 문제 

# 문제 요약 : 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원 동전이 무한히 존재
#            손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수 구하기 (단, 거슬러  줘야 할 돈은 항상 10의 배수)

N = 1260
count = 0

coin_list = [500, 100, 50, 10]

for coin in coin_list:
    count += N//coin
    N %= coin

print(count)
