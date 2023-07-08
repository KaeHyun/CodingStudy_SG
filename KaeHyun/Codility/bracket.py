# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # Implement your solution here
    temp = []
    if len(S) == 0 :
        return 1
    
    for i in S:
        if i == "(" or  i=="[" or i=="{":
            temp.append(i)
        elif len(temp) == 0 :
            return 0 

        if i ==  ")":
            latest =temp.pop()
            if latest != "(":
                return 0
        if i == "]":
            latest = temp.pop()
            if latest != "[":
                return 0 
        if i == "}":
            latest = temp.pop()
            if latest != "{":
                return 0
    if len(temp) == 0 :
        return 1
    else:
        return 0 



solution('{[()()]}')
solution('([)()]')