#프로그래머스
#자물쇠와 열쇠
#20이하이기 때문에 완전탐색으로 풀었습니다.
#무려 5중 포문.. 허허,,

def solution(key, lock):
    zero = 0
    
    #padding
    padding = len(key)-1
    padding_lock = [[2] * (len(lock) + padding*2) for _ in range(len(lock) + padding*2)]
    for i in range(len(lock)):
        for j in range(len(lock[0])):
            padding_lock[padding+i][padding+j] = lock[i][j]
            if lock[i][j] == 0:
                zero += 1
    
    #check
    for _ in range(4):
        key = rotate(key)
        for i in range(0, len(padding_lock)-padding):
            for j in range(0, len(padding_lock)-padding):
                ch = check(i, j, key, padding_lock, zero)
                if ch:
                    return True
    
    return False

def rotate(key):
    result = [[0] * len(key) for _ in range(len(key))]
    for i in range(len(key)):
        for j in range(len(key)):
            result[j][len(key)-1-i] = key[i][j]
    return result

def check(x, y, key, lock, zero):
    cnt = 0
    for i in range(len(key)):
        for j in range(len(key)):
            if lock[x+i][y+j] != key[i][j]:
                if lock[x+i][y+j] == 0:
                    cnt += 1
            else:
                return False
    if cnt == zero:
        return True 
    else:
        return False