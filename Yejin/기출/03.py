s = input()
res = 0

current = s[0]
for i in range(1, len(s)):
    if s[i] != current:
        res += 1
        current = s[i]

res //= 2
if s[0] != s[-1]:
    res += 1

print(res)