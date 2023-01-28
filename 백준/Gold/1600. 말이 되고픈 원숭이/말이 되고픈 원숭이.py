import sys
input = sys.stdin.readline
from collections import deque
# 말의 이동방법 
hx = [-2, -1, 1, 2, -2, -1, 1, 2]
hy = [1, 2, 2, 1, -1, -2, -2, -1] 
# 원숭이의 이동방법
mx = [0, 0, 1, -1]
my = [-1, 1, 0, 0]
def bfs(n) :
    dQ = deque()
    dQ.append((0, 0, n))
    #3차원 count리스트 count[x][y][남은 말처럼 이동 가능]
    count = [[[0] * (n+1) for _ in range(w)] for _ in range(h)]
    
    while dQ : 
        x, y, k = dQ.popleft()
        
        if x == h-1 and y == w-1 :
            return count[x][y][k]
        if k > 0 :
            for i in range(8) :
                xx = x + hx[i]
                yy = y + hy[i]
                if 0<=xx<h and 0<=yy<w :
                    if count[xx][yy][k-1] == 0 and board[xx][yy] == 0 :
                        count[xx][yy][k-1] = count[x][y][k]+1
                        dQ.append((xx, yy, k-1))
                    
        for i in range(4) :
            xx = x + mx[i]
            yy = y + my[i]
            if 0<=xx<h and 0<=yy<w :
                if count[xx][yy][k] == 0 and board[xx][yy]== 0 :
                    count[xx][yy][k] = count[x][y][k] + 1
                    dQ.append((xx, yy, k))
    return -1

# 원숭이가 최소한의 동작으로 시작점(0,0) -> 끝점(w-1, h-1) 갈 수 있는 최솟값
k = int(input()) # 말처럼 이동할 수 있는 횟수
w, h = map(int, input().split()) # w-가로길이, h-세로길이 
board = [list(map(int, input().split())) for _ in range(h)] # 0 - 평지, 1- 장애물
print(bfs(k))
