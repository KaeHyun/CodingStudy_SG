n = int(input())
coins = sorted(list(map(int, input().split())))
i = 1

for coin in coins:
    if coin <= i:
        i += coin
    else:
        break

print(i)
        