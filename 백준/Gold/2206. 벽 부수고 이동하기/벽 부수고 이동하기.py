#벽부수고이동하기. 
import sys
from collections import deque
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def bfs(i, j, cnt) :
    dQ = deque()
    dQ.append((i, j, cnt))
    
    while dQ :
        x, y, c = dQ.popleft()
        if x == n-1 and y == m-1 :
            return visited[x][y][c] 
        for i in range(4) :
            xx = x + dx[i]
            yy = y + dy[i]
            
            if xx < 0 or xx >= n or yy < 0 or yy >= m :
                continue
            
            if c == 0 and board[xx][yy] == 1 :
                visited[xx][yy][1] = visited[x][y][0] + 1
                dQ.append((xx, yy, 1))
                
            elif board[xx][yy] == 0 and visited[xx][yy][c] == 0 :
                visited[xx][yy][c] = visited[x][y][c] + 1
                dQ.append((xx, yy, c))
    return -1
                
        
n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1
print(bfs(0, 0, 0))
