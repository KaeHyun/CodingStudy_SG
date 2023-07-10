'''
이코테 312p (그리디 기출) 02 곱하기 혹은 더하기
0~9 로 이뤄진 문자열 S 왼쪽부터 하나씩 확인하며 x 또는 + 를 숫자사이에 
넣어서 만들 수 있는 가장 큰 수?
모든 연산은 왼쪽부터 수행됨

input : 02984 | 567
output : 576  | 210

'''
s = input()
nums = list(map(int,s))
cur = nums[0]

for i in range(1,len(nums)):
  if cur <= 1 or nums[i] <= 1:
    cur += nums[i]
  else:
    cur *= nums[i]
print(cur)
