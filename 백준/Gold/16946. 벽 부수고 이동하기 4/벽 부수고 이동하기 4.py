#벽 부수고 이동하기 4
import sys
from collections import deque
input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(i, j) :
    dQ = deque()
    dQ.append((i, j))
    cnt = 1 #현재 위치도 카운트 1
    visited[i][j] = 1 #시작위치 방문 표시***
    while dQ :
        x, y = dQ.popleft()
        zeros[x][y] = group
        for i in range(4) :
            xx = x + dx[i]
            yy = y + dy[i]
            if xx < 0 or xx >= n or yy < 0 or yy >= m : 
                continue
            elif board[xx][yy] == 0 and visited[xx][yy] == 0:
                visited[xx][yy] = 1 #방문체크
                dQ.append((xx, yy))
                cnt += 1 #0의 개수 카운트 
    return cnt 

def move_count(x, y) :
    aSet = set()
    #상하좌우 체크하면서 인접한 그룹 파악
    for i in range(4) : 
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<m :
            if zeros[xx][yy] != 0 :
                aSet.add(zeros[xx][yy])
    tmp = 1 #현재 위치 세기 
    for a in aSet :
        tmp += adict[a]
        tmp %= 10
    return tmp 
    
n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)] # 굳이 이게 필요한지??!! board로 커버 안되는가 체크 
zeros = [[0] * m for _ in range(n)] # group명 배열 
answer = [[0] * m  for _ in range(n)]
group = 1
adict = {}  # 그룹명 : 0의개수(=이동가능한영역)

#1. 0(=이동할 수 있는 영역)의 개수를 그룹별로 세기 
for i in range(n) :
    for j in range(m) :
        if board[i][j] == 0 and visited[i][j] == 0:
            adict[group] = bfs(i, j)
            group += 1

# 2. 1(=벽) 근처에 있는 그룹 체크 
for i in range(n) :
    for j in range(m) :
        if board[i][j] == 1 : #벽이면 -> board배열이 bfs이후에 또 필요함 -> visited를 사용해야 하는 이유임. (아예 방문표시를 -1로둬도가능함=겹치지 않도록  )
            answer[i][j] = move_count(i, j)
for i in range(n) :
    print("".join(map(str, answer[i])))