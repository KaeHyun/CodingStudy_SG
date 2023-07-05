'''
이코테 313p (그리디 기출) 03 문자열뒤집기
0과 1로 이뤄진 문자열 S. 
이 문자열 s에 있는 모든 숫자를 전부 같게 만들고자함.
할수있는 것 : 연속된 하나이상의 숫자들-> 모두 뒤집기
이 행동의 최소수?
input : 0001100
output : 1

'''

def flip(i):
  now = nums[i]
  while i < n and nums[i] == now:
    if now == '1':
      nums[i] = '0'
    else:
      nums[i] = '1'
    i += 1
    
nums = list(input())
n = len(nums)
result= 0 

while True:
  i = 0
  ones = 0
  zeros = 0
  # 다 0 이거나 1이면 break
  if len(set(nums)) == 1:
    break
  first1 = nums.index('1')
  first0 = nums.index('0')
  while i < n:
    # 01 중 블럭개수 더 적은 첫블럭 플립
    if nums[i] == '0':
      zeros += 1
      while i < n and nums[i] != '1':
        i += 1
    else:
      ones += 1
      while i < n and nums[i] != '0':
        i += 1
  if zeros <= ones :
    flip(first0)
  else :
    flip(first1)
  result += 1
print(result)
    
