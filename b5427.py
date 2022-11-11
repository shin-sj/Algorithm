import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [1,-1,0,0]
tc = int(input())
for _ in range(tc):
    w, h = map(int, input().split())
    board = [[x for x in input().rstrip()] for _ in range(h)] #빌딩 지도 
    fire = deque([]) #불
    sg = deque([]) #상근
    visited = [[False for _ in range(w)] for _ in range(h)] #상근이 방문한 곳 체크 
    for i in range(h):
        for j in range(w):
            if board[i][j] == "@": #상근의 현 위치
                sg.append([0, i, j]) 
                visited[i][j] = True #상근이 방문한 위치 방문 체크 
            elif board[i][j] == '*': #불 위치
                fire.append([i, j])
                board[i][j] = 0 #불이 있는 곳을 * -> 0으로 바꿈 
            elif board[i][j] == '#': #벽 
                visited[i][j] = True #벽은 갈 수 없으므로 방문 체크 
    while fire: #fire 먼저 돌리면서 불 날짜 체크 
        r, c = fire.popleft() 
        for i in range(4) :
            xx = r+dx[i]
            yy = c+dy[i]
            if 0 <= xx< h and 0 <= yy < w and board[xx][yy] == '.': #불이 번질 수 있는 공간이면 
                board[xx][yy] = board[r][c] + 1 #불이 번지는 것이 며칠째인지 
                fire.append([xx, yy])
    time = 0
    
    while sg: 
        t, r, c = sg.popleft()
        
        for i in range(4):
            xx = r+dx[i]
            yy = c+dy[i]
            if 0 <= xx < h and 0 <= yy < w: #지도를 벗어나지 않고 
                if not visited[xx][yy] and (board[xx][yy] == '.' or board[xx][yy] > t + 1): #갈수 있는 공간or불 번진시간보다 현재 시간이 앞인거! 
                    sg.append([t + 1, xx, yy])
                    visited[xx][yy] = True
            else: #지도 벗어나면 == 탈출 
                time = t + 1 #시간 계산 
                break

        if time:
            break
    if time:
        print(time)
    else:
        print("IMPOSSIBLE")