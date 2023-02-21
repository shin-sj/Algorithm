import sys
from collections import deque
input = sys.stdin.readline
dx = [0,0,-1,1]
dy = [1,-1,0,0]

        
m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
#1: 익은 토마토, 0:익지 않은 토마토, -1: 토마토가 들어있지 않은 칸
dQ = deque()
for i in range(n) :
    for j in range(m) :
        if board[i][j] == 1 :
            dQ.append((i, j)) #한번에 다 넣기 
            
while dQ :
    x, y = dQ.popleft()
    for k in range(4) :
        xx = x + dx[k]
        yy = y + dy[k]
        
        if 0<=xx<n and 0<=yy<m :
            if board[xx][yy] == 0 :
                board[xx][yy] = board[x][y] + 1
                dQ.append((xx, yy))
ans = 0
for i in range(n) :
    for j in range(m) :
        if board[i][j] == 0 :
            print(-1)
            exit(0)
        else :
            ans = max(ans, board[i][j])
print(ans-1)
                