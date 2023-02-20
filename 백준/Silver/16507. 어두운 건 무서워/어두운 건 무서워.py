import sys
input = sys.stdin.readline

R, C, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
dp = [[0 for _ in range(C+1)] for _ in range(R+1)]

for i in range(1, R+1) :
    for j in range(1, C+1) :
        #(1,1)~(i, j)의 밝기의 합
        dp[i][j] = -dp[i-1][j-1] + dp[i-1][j] + dp[i][j-1] + board[i-1][j-1] 

for i in range(Q) :
    r1, c1, r2, c2 = map(int, input().split())
    ans = dp[r2][c2] - dp[r1-1][c2] - dp[r2][c1-1] + dp[r1-1][c1-1] #(r1, c1) ~ (r2, c2)의 밝기 누적합
    num = ((r2 - r1) + 1) * ((c2 - c1) + 1) #구간에 속하는 픽셀의 개수 
    print(ans // num)