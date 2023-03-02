import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x) :
    if parent[x] != x : 
        parent[x] = find(parent[x])
    return parent[x]
def union(x,y) :
    x = find(x)
    y = find(y)
    if x < y :
        parent[y] = x
    else :
        parent[x] = y
    
n = int(input()) #도시의 수 
m = int(input()) #여행 계획에 속한 도시의 수 
parent = [i for i in range(n)]

for i in range(n) :
    alist = list(map(int, input().split()))
    for j in range(n) :
        if alist[j] == 1 :
            union(i, j)

parent = [-1] + parent
path = list(map(int, input().split()))
start = parent[path[0]]
for i in range(1, m) :
    if parent[path[i]] != start :
        print('NO')
        break
else :
    print('YES')