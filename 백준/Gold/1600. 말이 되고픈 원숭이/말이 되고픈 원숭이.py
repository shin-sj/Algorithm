#말이되고픈 원숭이 
import sys
from collections import deque
input = sys.stdin.readline
hx = [-2, -1, -2, -1, 1, 2, 1, 2]
hy = [1, 2, -1, -2, 2, 1, -2, -1]
mx = [0, 0, -1, 1]
my = [1, -1, 0, 0]
def bfs(i, j, cnt) :
    dQ = deque()
    dQ.append((i, j, cnt))
    
    while dQ :
        x, y, c = dQ.popleft()
        
        if x == h-1 and y == w-1 :
            return visited[x][y][c]
        if c < k :
            for i in range(8) : 
                xx = x + hx[i]
                yy = y + hy[i]
                if 0<=xx<h and 0<=yy<w :
                    if visited[xx][yy][c+1] == -1 and board[xx][yy] == 0 :
                        visited[xx][yy][c+1] = visited[x][y][c] + 1
                        dQ.append((xx, yy, c+1))
        for i in range(4) :
            xx = x + mx[i]
            yy = y + my[i]
            if 0<=xx<h and 0<=yy<w :
                if visited[xx][yy][c] == -1 and board[xx][yy] == 0 :
                    visited[xx][yy][c] = visited[x][y][c] + 1
                    dQ.append((xx, yy, c)) 
    return -1
    
k = int(input()) #말처럼 움직일 수 있는 횟수 
w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)] 
visited = [[[-1] * (k+1) for _ in range(w)] for _ in range(h)]

visited[0][0][0] = 0 #본인 위치 세어야 하나요..?
print(bfs(0, 0, 0))
