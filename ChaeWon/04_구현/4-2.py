'''
예제 4-2 시각
정수 N이 입력되면 00시 00분 00초 ~ N시 59분 59초까지 중 3이 하나라도 포함되는 시각의 수
input 5 output 11475

~ data 개수가 100만 개 이하(2초)일 때 완전 탐색을 사용하면 적절하다. ~

'''

n = int(input())
time = [0,0,0]
result = 0
while time != [n,59,59]:
  time[2] += 1
  if time[2] == 60:
    time[1] += 1
    time[2] = 0
    if time[1] == 60:
      time[0] += 1
      time[1] = 0      
  if '3' in ''.join(map(str,time)):
    result += 1
print(result)
