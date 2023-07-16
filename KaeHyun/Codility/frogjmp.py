# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # Implement your solution here
    togo = Y - X
    q =togo // D
    # print(q)
    r = togo % D
    # print(r)
    if r == 0:
        return q
    else:
        return q+1

solution(10, 85, 30)