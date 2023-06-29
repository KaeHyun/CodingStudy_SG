# 예제 3-3 숫자 카드 게임
'''
여러개의 숫자 카드 중 가장 높은 숫자가 쓰인 카드 한장을 뽑는 게임
N 행 개수 M 열 개수
선택한 행의 가장 숫자가 낮은 카드를 뽑을 것을 고려해 최종적으로 가장 높은 숫자의 카드를 뽑도록
(1)
input        output : 2
3 3
3 1 2
4 1 4
2 2 2
(2)
input        output : 3
2 4
7 3 1 8
3 3 3 4  

'''
# 해당 행의 min 가 가장 큰 행을 골라 뽑을 것
n, m = map(int,input().split())
data = []
for _ in range(n):
  data.append(list(map(int,input().split())))
  
mins = [ min(d) for d in data ]
print(max(mins))
