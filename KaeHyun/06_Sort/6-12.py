# 두 배열의 원소 교체 
# 문제 요약: K 번의 바꿔치기를 이용해서 배열 A의 모든 원소의 합의 최댓값을 반환

N, K = map(int, input().split()) # N 개의 원소로 이루어진 배열, K 번의 바꿔치기 가능

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for _ in range(K):
    if A[0] < B[0]:
        A.pop(0)
        A.append(B[0])
        B.pop(0)
        A.sort()
        B.sort(reverse=True)

print(sum(A))
