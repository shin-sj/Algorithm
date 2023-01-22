import sys
input = sys.stdin.readline

n, m = map(int, input().split())
alist = list(map(int, input().split()))
lt = max(alist)
rt = sum(alist)

while lt <= rt:
    mid = (lt + rt) // 2
    cnt = 0
    temp = 0
    for i in range(n):
        if temp + alist[i] > mid:
            cnt += 1
            temp = 0
        temp += alist[i]

    cnt += 1 if temp else 0

    if cnt <= m:
        rt = mid - 1
    else:
        lt = mid + 1
print(lt)