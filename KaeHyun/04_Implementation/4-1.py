# 상하좌우

# 문제 요약: 사용자가 도착하는 최종 좌표 return 하기 

# 5
# R R R U D D

n =  int(input())
togo = list(map(str, input().split()))

user = [1,1]

for i in togo:
    if i == "L":
        if user[1] - 1 >= 1 and user[1] - 1 <= n:
            user[1] -= 1
    if i == "R" :
        if user[1]+1 >= 1 and user[1] + 1 <= n:
            user[1] +=1 
    if i == "U":
        if user[0] -1 >=1 and user[0] -1 <=n :
            user [0] -=1
    if i == "D":
        if user[0] +1 >=1 and user[0] +1 <=n:
            user[0] +=1  

#좌표 공백으로 출력     
print(' '.join(map(str,user)))
