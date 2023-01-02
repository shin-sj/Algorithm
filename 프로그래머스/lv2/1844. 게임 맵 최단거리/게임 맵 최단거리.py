import sys
from collections import deque
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(maps) : 
    xend = len(maps)
    yend = len(maps[0])
    dQ = deque()
    dQ.append((0,0))
    while dQ : 
        x, y = dQ.popleft()
        for i in range(4) :
            xx = x + dx[i]
            yy = y + dy[i] 
            if 0<=xx<xend and 0<=yy<yend :
                if maps[xx][yy] == 1 :
                    maps[xx][yy] = maps[x][y] + 1
                    dQ.append((xx, yy))
                    
def solution(maps):
    answer = 0
    xend = len(maps)
    yend = len(maps[0])
    if xend == 1 and yend == 1 :
        return 1
    bfs(maps)
    if maps[xend-1][yend-1] == 1 :
        return -1
    else :
        return maps[xend-1][yend-1]