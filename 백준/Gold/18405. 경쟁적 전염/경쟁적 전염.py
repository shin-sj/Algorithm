from collections import deque

n, k = map(int, input().split())
board = [] # 전체 맵 정보 담는 리스트
data = [] # 바이러스 정보를 담는 리스트
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j] != 0:
            # 바이러스 숫자, x위치, y위치, 시간 을 입력받는다.
            data.append((board[i][j], i, j, 0))

S, X, Y = map(int, input().split())
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

data.sort()
dQ = deque(data)

while dQ:
    virus, x, y, time = dQ.popleft()
    if time == S:
        break
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= mx < n and 0 <= my < n:
            if board[mx][my] == 0:
                board[mx][my] = virus
                dQ.append((virus, mx, my, time+1))

print(board[X-1][Y-1])