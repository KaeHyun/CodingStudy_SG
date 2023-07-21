#문자열 재정렬
string = [i for i in input()]
string.sort()
num = 0
index = 0
for i in string:
    try:
        num += int(i)
        index += 1
    except:
        pass

print(''.join(string[index:]), end='')
print(num)