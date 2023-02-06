import sys
input = sys.stdin.readline

n, k = map(int, input().split()) #n:주전자수, k:친구수
alist = []
for _ in range(n) :
    alist.append(int(input())) #주전자의 용량 list
alist.sort() 
lt = 1
rt = alist[-1]
ans = 0
while lt <= rt :
    mid = (lt+rt) // 2 
    cnt = 0 
    for a in alist :
        cnt += a // mid 
    if cnt >= k :
        ans = mid
        lt = mid + 1
    else :
        rt = mid - 1
print(ans)
