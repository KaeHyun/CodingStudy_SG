# 럭키 스트레이트
score = [int(i) for i in input()]
mid = len(score)//2

if sum(score[:mid]) == sum(score[mid:]):
    print('LUCKY')
else:
    print('READY')