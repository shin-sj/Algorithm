import sys
from collections import deque
input = sys.stdin.readline
hx = [-2,-1,-2,-1,1,2,1,2]
hy = [1,2,-1,-2,2,1,-2,-1]
mx = [0,0,1,-1]
my = [1,-1,0,0]
def bfs(i, j, cnt) :
    dQ = deque()
    dQ.append((i, j, cnt))
    while dQ :
        x,y,c = dQ.popleft()
        if x == H-1 and y == W-1 :
            return visited[x][y][c]
        if c < k :
            for i in range(8) :
                xx = x + hx[i]
                yy = y + hy[i] 
                if 0<=xx<H and 0<=yy<W :
                    if visited[xx][yy][c+1] == -1 and board[xx][yy] == 0 :
                        visited[xx][yy][c+1] = visited[x][y][c] + 1
                        dQ.append((xx, yy, c+1))
        for i in range(4) :
            xx = x + mx[i]
            yy = y + my[i]
            if 0<=xx<H and 0<=yy<W :
                if visited[xx][yy][c] == -1 and board[xx][yy] == 0 :
                    visited[xx][yy][c] = visited[x][y][c] + 1
                    dQ.append((xx, yy, c))
    return -1
                
k = int(input()) #말처럼 움직일 수 있는 횟수
W, H = map(int, input().split()) #W-가로길이, H-세로길이
board = [list(map(int, input().split())) for _ in range(H)]
visited = [[[-1] * (k+1) for _ in range(W)] for _ in range(H)]
visited[0][0][0] = 0 
#맨 왼쪽 위에서 시작해서 맨 오른쪽 아래까지
#원숭이가 최소한의 동작으로 시작지점에서 도착지점까지 갈 수 있는 방법
print(bfs(0,0,0))