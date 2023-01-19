#1926 그림 - dfs
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x, y) : 
    global img_area
    for i in range(4) :
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<m : 
            if board[xx][yy] == 1 :
                board[xx][yy] = 0 #방문 표시 
                img_area += 1 #그림의 넓이 계산 
                dfs(xx, yy)

n, m = map(int, input().split()) #n-세로, m-가로
board = [list(map(int, input().split())) for _ in range(n)]
img_cnt = 0 #그림의 개수 
max_area = 0 #가장 넓은 그림의 넓이 

for i in range(n) :
    for j in range(m) :
        if board[i][j] == 1 :
            img_area = 1 #그림의 넓이 초기화 
            board[i][j] = 0
            dfs(i, j)
            img_cnt += 1 #그림의 개수 세기(덩어리) 
            max_area = max(max_area, img_area)
print(img_cnt) #그림의 개수 출력 
print(max_area) #넓이의 최대값 출력 