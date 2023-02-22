import sys
input = sys.stdin.readline

n = int(input())
start, end = 0, 0
ans = 0
while start <= end and end <= n :
    atemp = [i for i in range(start, end+1)]
    asum = sum(atemp)
    if asum == n :
        ans += 1
        end += 1
    elif asum < n :
        end += 1
    else :
        start += 1
print(ans)
    
    