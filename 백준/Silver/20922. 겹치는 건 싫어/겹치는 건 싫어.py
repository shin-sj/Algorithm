import sys
input = sys.stdin.readline

n, k = map(int, input().split()) 
alist = list(map(int, input().split()))
lt, rt = 0, 0
check = [0] * 100001
answer = 0
cnt = 0

while rt < n:
    if check[alist[rt]] < k:
        check[alist[rt]] += 1
        cnt += 1
        rt += 1
    else:
        answer = max(answer, cnt)
        cnt -= 1
        check[alist[lt]] -= 1
        lt += 1
answer = max(answer,cnt)
print(answer)