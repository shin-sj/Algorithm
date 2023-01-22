#보물섬 - bfs, bruteforce
import sys
from collections import deque
input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(i, j) :
    dQ = deque()
    dQ.append((i, j))
    visited = [[0] * w for _ in range(h)]
    visited[i][j] = 1
    cnt = 0
    while dQ :
        x, y = dQ.popleft()
        for i in range(4) :
            xx = x + dx[i]
            yy = y + dy[i]
            if xx < 0 or xx >= h or yy < 0 or yy >= w :
                continue
            elif board[xx][yy] == 'L' and visited[xx][yy] == 0 :
                visited[xx][yy] = visited[x][y] + 1 #거리체크 
                cnt = max(cnt, visited[xx][yy])
                dQ.append((xx, yy))
    return cnt-1

h, w = map(int, input().split())
board = [list(map(str, input().rstrip())) for _ in range(h)]
answer = 0

#L육지에서 출발 -> 최단거리가 젤 긴거 
for i in range(h) :
    for j in range(w) :
        if board[i][j] == 'L' :
            answer = max(answer, bfs(i, j))
print(answer)