import sys
input = sys.stdin.readline

n, m = map(int, input().split())
alist = list(map(int, input().split()))
lt, rt = 0, 0
cnt = 0
while lt <= rt and rt <= n :
    asum = sum(alist[lt:rt])
    if asum == m :
        cnt += 1
        lt += 1
    elif asum < m :
        rt += 1
    else :
        lt += 1
print(cnt)