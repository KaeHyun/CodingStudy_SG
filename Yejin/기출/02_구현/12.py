# 기둥과 보 설치
# 프로그래머스 60061
# 아무리 풀어도 안돼서 답 참고함ㅜㅠ

def solution(n, build_frame):
    result = []
    # [가로, 세로, 기둥/보, 삭제/설치]
    # 0 기둥, 1 보
    # 0 삭제, 1 설치
    
    for i in build_frame:
        if i[3] == 0: # 삭제
            result.remove([i[0], i[1], i[2]])
            if not possible(result):
                result.append([i[0], i[1], i[2]])
            
        else: # 설치
            result.append([i[0], i[1], i[2]])
            if not possible(result):
                result.remove([i[0], i[1], i[2]])
    
    return sorted(result)

def possible(result):
    for i in result:
        x, y = i[0], i[1]
        if i[2] == 0: #기둥
            if y == 0 or [x-1, y, 1] in result or [x, y, 1] in result or [x, y-1, 0] in result:
                continue
            else:
                return False
        if i[2] == 1: #보
            if [x, y-1, 0] in result or [x+1, y-1, 0] in result or ([x-1, y, 1] in result and [x+1, y, 1] in result):
                continue
            else:
                return False
    return True
    