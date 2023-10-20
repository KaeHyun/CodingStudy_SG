def solution(clothes):

    clothing = dict()
    for c in clothes:
        item, key = c
        if key in clothing:
            clothing[key].append(item)
        else:
            clothing[key] = [item]
    # 딕셔너리 길이 = key 개수 

    with_items = 1
    for key, value in clothing.items():
        with_items *= (len(value)+1) # 아무것도 안 입는 경우 포함 
    return with_items-1 # 전부 안 입은 경우 제외 

    