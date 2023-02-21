import sys
from collections import deque
input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(i, j) :
    dQ = deque()
    dQ.append((i, j))
    while dQ :
        x, y = dQ.popleft()
        if x == n-1 and y == m-1 :
            return visited[x][y]
        for k in range(4) :
            xx = x + dx[k]
            yy = y + dy[k]
            if 0<=xx<n and 0<=yy<m :
                if visited[xx][yy] == 0 and board[xx][yy] == 1 :
                    visited[xx][yy] = visited[x][y] + 1
                    dQ.append((xx, yy))
    
n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
visited[0][0] = 1 #현재 위치도 count 
print(bfs(0,0))