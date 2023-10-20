
# 'A' = 65, 'Z' = 90

def solution(name):

    answer = 0 

    min_cursor = len(name) -1 

    for idx, char in enumerate(name):

        answer += min(ord(char) - ord("A"), ord("Z") - ord(char) + 1) # 알파벳 변경 횟수 
        
        isA = idx +1 # 해당 알파벳 다음부터 연속된 A가 존재하는지?
        
        while isA < len(name) and name[isA] == 'A':
            # 다음 index에도 A가 있는지 확인
            isA +=1 
        
        #  # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        min_cursor = min([min_cursor, 2 *idx + len(name) - isA, idx + 2 * (len(name) -isA)])
    
    return answer + min_cursor

solution('JGAAEQAZ')
solution("JAN")
solution("JEROEN")