# def solution(s):
#     answer = []
#     answer.append(-1)
#     for i in range(1, len(s)) :
#         print(s[:i+1])
#         if s[i] not in s[:i] :
#             answer.append(-1)
#         else  : #존재하면  
#             alist = list(filter(lambda x : s[x] == s[i], range(i)))
#             # tmp = s[:i].index(s[i]) #앞의 원소가 몇번째인지?
#             answer.append(i - alist[-1])
#     return answer
def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i
    return answer