def solution(clothes):
    answer = 1
    #각 카테고리별로 +1 한 것을 모두 곱한 후 답에서 -1 하기. 
    # { headgear : 2, eyewear : 1 } 
    adict  = {}
    for i in range(len(clothes)) :
        if clothes[i][1] in adict :
            adict[clothes[i][1]] += 1
        else : #없으면 새로 딕셔너리에 넣기. 
            adict[clothes[i][1]] = 1
    for value in adict.values() :
        answer *= (value+1)
        print(answer)        
    
    return answer-1