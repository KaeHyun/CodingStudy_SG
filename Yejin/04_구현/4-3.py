start = input()
count = 0

row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

dx = [2, 2, -2, -2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, 2, 2, -2, -2]
x, y = row.index(start[0]), int(start[1])-1

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<=8 and 0<=ny<=8:
        count += 1

print(count)