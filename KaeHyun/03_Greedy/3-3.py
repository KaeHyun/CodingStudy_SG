# 숫자 카드 게임

# 문제 요약: 숫자 카드를 N X M [행 X 열] 형태로 두고 뽑고자 하는 행 선택
#           선택된 행에서 가장 숫자가 낮은 카드 뽑기 -> 이 뽑을 수 있는 게 가장 큰 값이면 됨


n, m = map(int, input().split())

answer = 0

for i in range(n):
    cards = list(map(int, input().split()))
    min_num = min(cards)
    if min_num > answer:
        answer = min_num

print(answer)