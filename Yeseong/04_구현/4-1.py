n = int(input())
plans = input().split()
x, y = 1, 1

for plan in plans:
    if plan == 'L':
        if y != 1:
            y -= 1
    elif plan == 'R':
        if y != n:
            y += 1
    elif plan == 'U':
        if x != 1:
            x -= 1
    elif plan == 'D':
        if x != n:
            x += 1
            
print(x, y)  
        