import sys
input = sys.stdin.readline

direction = dict()
direction['D']=[0,1]
direction['L']=[-1,0]
direction['R']=[1,0]
direction['U']=[0,-1]

N, M = map(int,input().split())
field = [list(input().strip()) for _ in range(N)]
parent = [i for i in range(N * M)]

def find(x) :
    if x == parent[x] :
        return x
    parent[x] = find(parent[x])
    return parent[x]
def unionParent(a, b) :
    a = find(a)
    b = find(b)
    if a == b :
        return
    if a < b :
        parent[b] = a
    else :
        parent[a] = b
for num in range(N * M):
    x = num % M
    y = num // M
    cur = field[y][x]
    nx = x + direction[cur][0]
    ny = y + direction[cur][1]
    next_num = ny * M + nx
    if next_num < 0 or next_num >= N * M:
        continue
    unionParent(num, next_num)
answer = 0
visited = dict()
for i in range(N * M):
    if find(parent[i]) not in visited :
        answer += 1
        visited[parent[i]] = True
print(answer)