import sys
from itertools import combinations
input = sys.stdin.readline

n, s = map(int, input().split()) 
alist = list(map(int, input().split()))
ans = 0
for i in range(1, n+1) :
    comb = combinations(alist, i)
    
    for i in comb :
        if sum(i) == s :
            ans += 1
print(ans)