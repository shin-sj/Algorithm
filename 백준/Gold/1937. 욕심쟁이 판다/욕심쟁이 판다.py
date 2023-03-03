import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def dfs(x, y):
    if dp[x][y] : 
        return dp[x][y] # 이미 한번 왔다간 경로는 그대로 리턴
    dp[x][y] = 1 #1부터 시작 
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<n :
            if board[x][y] < board[xx][yy] :
                dp[x][y] = max(dp[x][y], dfs(xx, yy) + 1)
    return dp[x][y]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))

print(answer)