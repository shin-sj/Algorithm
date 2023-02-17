from itertools import permutations
def ch(n) :
    if n < 2 :
        return False
    for i in range(2, int(n**0.5) + 1) :
        if n % i == 0 :
            return False
    return True

def solution(numbers):
    answer = []
    tmp = []
    for i in range(1, len(numbers)+1) :
        tmp.extend(permutations(numbers, i))
    real = [int(''.join(t)) for t in tmp]
    for r in real :
        if ch(r) :
            answer.append(r)

    return len(set(answer))