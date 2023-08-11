n = int(input())
people = sorted(list(map(int, input().split())))
group = 0
idx = 0

while(idx < n):
    count = 0
    p = people[idx]
    for i in people[idx:idx+p]:
        if i <= p:
            count += 1
    if count == p:
        group += 1
        idx = idx+p
    else:
        idx += 1
    
print(group)