# 성적이 낮은 순서로 학생 출력하기

N = int(input()) # 학생 수 
info = []

for i in range(N):
    a, b = map(str, input().split())
    info.append((a,int(b))) 

info = sorted(info, key = lambda name : name[1]) #내림차순 정렬하고 싶으면, lambda name: -name[1]

for i in info:
    print(i[0], end=' ')
