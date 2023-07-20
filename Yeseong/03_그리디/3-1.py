N = int(input()) # 단, 항상 10의 배수
cnt = 0

coins = [500, 100, 50, 10]

for coin in coins:
    cnt += N // coin # 몫
    N %= coin # 남은 거스름돈 update
    
print(cnt)