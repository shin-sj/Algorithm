import sys
from collections import Counter
def solution(participant, completion):
    answer = ''
    par = Counter(participant)
    com = Counter(completion) 
    
    for i in range(len(completion)) :
        if par[completion[i]] == com[completion[i]] : 
            del par[completion[i]]
    return (list(par)[0])