import sys
from collections import deque
input = sys.stdin.readline

A, B, N, M = map(int, input().split())
#A, B - 스카이 콩콩의 힘 
#N, M - 동규와 주미의 현재위치 

#동규가 주미에게 도달하기 위한 최소한의 이동 횟수는?
visited = [-1] * 100001

dQ = deque()
visited[N] = 0
dQ.append(N) 

while dQ :
    now = dQ.popleft()
    if now == M :
        break

    if 0<=now+1<100001 and visited[now+1] == -1 :
        visited[now+1] = visited[now] + 1
        dQ.append(now+1)
    if 0<=now-1<100001 and visited[now-1] == -1 :
        visited[now-1] = visited[now] + 1
        dQ.append(now-1)
    if 0<=now+A<100001 and visited[now+A] == -1 :
        visited[now+A] = visited[now] + 1
        dQ.append(now+A)
    if 0<=now-A<100001 and visited[now-A] == -1 :
            visited[now-A] = visited[now] + 1
            dQ.append(now-A)
    if 0<=now+B<100001 and visited[now+B] == -1 :
        visited[now+B] = visited[now] + 1
        dQ.append(now+B)
    if 0<=now-B<100001 and visited[now-B] == -1 :
        visited[now-B] = visited[now] + 1
        dQ.append(now-B)   
    if 0<=now*A<100001 and visited[now*A] == -1 :
        visited[now*A] = visited[now] + 1
        dQ.append(now*A)
    if 0<=now*B<100001 and visited[now*B] == -1 :
        visited[now*B] = visited[now] + 1
        dQ.append(now*B)
        
print(visited[M])