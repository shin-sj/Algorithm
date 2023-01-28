#특정 거리의 도시 찾기
import sys
from collections import deque
input = sys.stdin.readline
def dfs(start) :
    dQ = deque()
    dQ.append(start)
    visited[start] = 1
    cnt = 0
    while dQ:
        s = dQ.popleft()
        for i in graph[s] :
            if visited[i] == 0 :
                visited[i] = 1 #방문 표시 
                distance[i] = distance[s] + 1
                dQ.append(i)

#n도시의개수, m도로의개수, k거리정보, x출발도시정보
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [0] * (n+1)
visited = [False] * (n+1)
# print(graph)
for _ in range(m) :
    a,b = map(int, input().split())
    graph[a].append(b)
dfs(x)
flag = 0
for i in range(1, n+1) :
    if distance[i] == k :
        print(i)
        flag = 1
if flag ==0 :
    print(-1)
