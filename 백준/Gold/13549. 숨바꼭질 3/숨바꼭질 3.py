#숨바꼭질3
import sys
from collections import deque
MAX = 100001
input = sys.stdin.readline

n, k = map(int, input().split()) #n-수빈위치, m-동생위치
visited = [-1] * MAX

dQ = deque()
dQ.append(n) 
visited[n] = 0

while dQ :
    x = dQ.popleft()
    if x == k :
        print(visited[k])
        break
 
    if 0 <= x * 2 < MAX and visited[x * 2] == -1 :
        visited[x * 2] = visited[x]
        dQ.appendleft(x * 2) # x * 2 가 다른 연산보다 더 높은 우선순위를 가지기 위함
    if 0 <= x - 1 < MAX and visited[x - 1] == -1 :
        visited[x - 1] = visited[x] + 1
        dQ.append(x - 1)
    if 0 <= x + 1 < MAX and visited[x + 1] == -1 :
        visited[x + 1] = visited[x] + 1
        dQ.append(x + 1)