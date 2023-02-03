#촌수 계산
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start) : 
    dQ = deque()
    dQ.append(start)
    while dQ :
        start1 = dQ.popleft() 
        for i in graph[start1] :
            if visited[i] == -1 :
                visited[i] = visited[start1]+1
                dQ.append(i)
    
n = int(input()) #사람 수 
x, y = map(int, input().split()) # 촌수 계산해야하는 두사람의 번호
m = int(input()) #관계의 개수
graph = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited[x] = 0
bfs(x)
print(visited[y])
