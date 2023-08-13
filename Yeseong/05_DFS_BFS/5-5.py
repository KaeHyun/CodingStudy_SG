n = int(input())

# 반복적
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 재귀적
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

print('반복적 구현: ', factorial_iterative(n))
print('재귀적 구현: ', factorial_recursive(n))