# 큰 수의 법칙 
# 문제 요약 : 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙 (단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징)

n, m, k = map(int, input().split()) #N : 배열의 크기 , M : 숫자가 더해지는 횟수, K: 연속해서 더해질 수 있는 제한
num_array= list(map(int, input().split()))
num_array.sort(reverse=True)
max_num = num_array[0]
sec_num = num_array[1]

answer = 0
# while True:

#     for i in range(k):
#         if m == 0 :
#             break
#         #가장 큰 숫자 우선 더하기
#         answer += max_num
#         m -= 1
#     if m == 0:
#         break
#     answer += sec_num # 두 번째 숫자는 한 번만
#     m -=1

# print(answer)

# 반복문을 사용하지 않는 2번째 솔루션

count = int(m/(k+1)) 
remain = m%(k+1) 

answer += max_num*count*k
answer += sec_num*count
answer += max_num*remain
print(answer)
