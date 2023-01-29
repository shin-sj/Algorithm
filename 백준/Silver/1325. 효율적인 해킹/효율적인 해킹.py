import sys
from collections import deque
input = sys.stdin.readline

def bfs(start) :
    dQ = deque()
    dQ.append(start)
    visited[start] = 1
    
    while dQ :
        start = dQ.popleft()
        for c in computer[start] : 
            if visited[c] == 0 :
                visited[c] = 1
                dQ.append(c)
         
n, m = map(int, input().split()) #n-컴퓨터의 개수, m-신뢰하는관계 수
computer = [ [0] for i in range(n+1) ]
cnt = [] 
for _ in range(m) :
    a, b = map(int, input().split())
    computer[b].append(a)

for i in range(1, n+1) :
    visited = [0] * (n+1)
    bfs(i) 
    cnt.append(visited.count(1)) #1이 몇개인지 
    
idx  = 1
for c in cnt : 
    if c == max(cnt) :
        print(idx , end=' ')
    idx  += 1