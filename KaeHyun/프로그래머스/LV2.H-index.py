# 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고
# 나머지 논문이 h번 이하 인용되었다면
# h의 최댓값이 이 과학자의 h-index

def solution(citations):
    answer = 0
    
    h_index = sum(citations) // len(citations)
    count = 0
    while count < h_index:
        for i in range(len(citations)):
            if citations[i] >= h_index:
                count +=1
        if count >= h_index:
            answer = h_index
        else:
            if h_index < 0:
                h_index = 0 
            h_index -=1
            count = 0
        
    return answer