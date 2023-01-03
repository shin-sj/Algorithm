def solution(t, p):
    answer = 0
    alist = []
    print(len(t) - len(p) + 1)

    for i in range(len(t) - len(p) + 1) :
        tmp = t[i:i+len(p)]
        alist.append(tmp)
    print(alist)
    for a in alist :
        if a <= p :
            answer += 1
    return answer