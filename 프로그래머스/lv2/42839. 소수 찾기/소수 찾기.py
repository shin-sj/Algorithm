from itertools import permutations
def ch(n) :
    if n < 2 :
        return False
    for i in range(2, int(n**0.5)+1 ) :
        if n % i == 0 :
            return False
    return True

def solution(numbers):
    answer = []
    alist = []
    for i in range(1, len(numbers)+1) :
        alist.extend(permutations(numbers, i))
    real = [int(''.join(t)) for t in alist]
    for a in real :
        if ch(a) :
            answer.append(a)
    
    return len(set(answer))

# from itertools import permutations
# def cal(n) :
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1) :
#         if n % i == 0 :
#             return False
#     return True
        
# def solution(numbers):
#     answer = 0
#     tmp =[]
#     for i in range(1, len(numbers)+1) :
#         tmp.extend(permutations(numbers, i))
#     real = [int(''.join(t)) for t in tmp]
           
#     for a in real :
#         if cal(a) :
#             answer += 1
#     return answer