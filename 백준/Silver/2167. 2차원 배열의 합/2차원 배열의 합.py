import sys
input = sys.stdin.readline

n, m = map(int, input().split()) #배열의 크기 n, m
board = [list(map(int, input().split())) for _ in range(n)]
k = int(input()) #합을 구할 부분의 개수
ans = [] #답 배열
for _ in range(k) :
    i, j, x, y = map(int, input().split())
    sum = 0
    for p in range(i-1, x) :
        for q in range(j-1, y) :
            sum += board[p][q]
    ans.append(sum)
for an in ans :
    print(an)
