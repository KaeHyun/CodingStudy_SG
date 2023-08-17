n = int(input())

array = []
for i in range(n):
    scores = input().split()
    array.append((scores[0], int(scores[1])))
    
array.sort(key=lambda data: data[1])

for d in array:
    print(d[0], end=' ')