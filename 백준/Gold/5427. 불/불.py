import sys
input = sys.stdin.readline
from collections import deque
dx = [0,0,-1,1]
dy = [1,-1,0,0]

tc = int(input())
for _ in range(tc) :
    w, h = map(int, input().split()) 
    board = [[x for x in input().rstrip()] for _ in range(h)] #빌딩 지도 
    fire = deque([]) #불
    sg = deque([]) # 상근 
    visited = [[0] * w for _ in range(h)]
    
    for i in range(h) :
        for j in range(w) :
            if board[i][j] == '@' : #상근의 현 위치
                visited[i][j] = 1
                sg.append([0,i,j])
            elif board[i][j] == '*' : #불의 위치
                fire.append([i,j])
                board[i][j] = 0
            elif board[i][j] == '#' : #벽
                visited[i][j] = 1

    #불 위치 
    while fire :
        x, y = fire.popleft() 
        for i in range(4) :
            xx = x + dx[i]
            yy = y + dy[i]
            
            if 0<=xx<h and 0<=yy<w and board[xx][yy] == '.' :
                board[xx][yy] = board[x][y] + 1
                fire.append([xx, yy])
    
    time = 0
    while sg :
        t, x, y = sg.popleft()
        for i in range(4) :
            xx = x + dx[i]
            yy = y + dy[i] 
            
            if 0<=xx<h and 0<=yy<w :
                if visited[xx][yy] == 0 and (board[xx][yy] == '.' or board[xx][yy] > t+1) :
                    sg.append([t+1, xx, yy])
                    visited[xx][yy] = 1
            else : 
                time = t+1
                break
        if time :
            break
    if time :
        print(time) 
    else :
        print("IMPOSSIBLE")
        
       