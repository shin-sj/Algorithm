import sys
from collections import deque
input = sys.stdin.readline
def bfs(i) : 
    dQ = deque()
    dQ.append(i)
    
    while dQ :
        x = dQ.popleft()
        for j in board[x] :
            if visited[j] == -1 :
                visited[j] = visited[x] + 1
                dQ.append(j)
    
# n-도시의 개수, m-도로의 개수, k-거리 정보, x-출발도시의 번호
n, m, k, x = map(int, input().split()) 
board = [[] for _ in range(n+1)]

for _ in range(m) :
    # a -> b 단방향 도로 
    a, b = map(int, input().split())
    board[a].append(b)

# X로부터 출발하여 도달할 수 있는 도시 중에서
# 최단 거리가 K인 모든 도시의 번호
visited = [-1] * (n+1)
visited[x] = 0
bfs(x)
flag = 0
for i in range(1, len(visited)) :
    if visited[i] == k :
        print(i)
        flag = 1
if flag == 0 :
    print(-1)
