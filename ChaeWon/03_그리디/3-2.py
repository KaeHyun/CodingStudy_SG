# 예제 3-2 큰 수의 법칙
'''
n개의 수로 이뤄진 배열이 있을 때 
주어진 수들을 M번 더해 가장큰 수를 만드는 법칙
단 특정 인덱스 수를 k번 초과해 연속으로 더할 수 없음
''' 
n, m, k = map(int,input().split())
data = list(map(int,input().split()))
data.sort(reverse=True)
fir = data[0]
sec = data[1]

# 구성 : 젤 큰수 k 개 + 두번째 큰수 1개 묶음 반복 
myset = [fir]*k + [sec]
count = m // (k+1)
namerge = m % (k+1)
result = count * sum(myset) + sum(myset[:namerge])

print(result)
