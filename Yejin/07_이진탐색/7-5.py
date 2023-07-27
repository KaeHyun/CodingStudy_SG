# 부품 찾기
n = int(input())
stock = list(map(int, input().split()))
m = int(input())
need = list(map(int, input().split()))
            
for i in need:
    if i in stock:
        print("yes")
    else:
        print("no")