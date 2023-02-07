import sys
from itertools import combinations
input = sys.stdin.readline
check =  [0]*2000001
check[0] = 1
n = int(input())
s =  list(map(int, input().split()))

for i in range(1, n + 1): 
    for j in combinations(s, i): 
        check[sum(j)] = 1
print(check.index(0))