import sys
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(maps) :
    dQ = deque()
    maps[0][0] = 1 #방문 표시
    dQ.append((0, 0))
    xend = len(maps)
    yend = len(maps[0])
    while dQ : 
        x, y = dQ.popleft()
        if x == xend-1 and y == yend-1 :
            return maps[x][y]
        for i in range(4) :
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<xend and 0<=yy<yend :
                if maps[xx][yy] == 1 :
                    maps[xx][yy] = maps[x][y] + 1
                    dQ.append((xx, yy))
    return -1
            
    
def solution(maps):
    answer = 0
    xend = len(maps)
    yend = len(maps[0])
     
    return bfs(maps)