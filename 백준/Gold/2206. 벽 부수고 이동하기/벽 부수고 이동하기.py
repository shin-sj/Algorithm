import sys
from collections import deque
input = sys.stdin.readline
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(a, b, c) :
    dQ = deque()
    dQ.append((a, b, c))
    
    while dQ :
        x, y, z =dQ.popleft()
        
        if x == n-1 and y == m-1 :
            return visited[x][y][z]
        
        for i in range(4) :
            xx = x + dx[i]
            yy = y + dy[i]
            
            if xx < 0 or xx >= n or yy < 0 or yy >= m :
                continue
            #벽 + 부술 수 있는 경우
            if board[xx][yy] == 1 and z == 0 :
                visited[xx][yy][1] = visited[x][y][0] + 1
                dQ.append((xx, yy, 1))
            elif board[xx][yy] == 0 and visited[xx][yy][z] == 0 :
                visited[xx][yy][z] = visited[x][y][z] + 1
                dQ.append((xx, yy, z))
    return -1
    
n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
# print(visited)
visited[0][0][0] = 1 #시작 방문 표시
print(bfs(0, 0, 0))
