h = int(input())

cnt = 0

for i in range (h + 1):
    for m in range(60):
        for s in range(60):
            if '3' in str(i) or '3' in str(m) or '3' in str(s):
                cnt += 1
                
print(cnt)