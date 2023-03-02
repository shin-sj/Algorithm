import sys
input = sys.stdin.readline

n, m = map(int, input().split())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))
ans = []
lt = 0
rt = 0

while lt < n and rt < m :
    if alist[lt] < blist[rt] :
        ans.append(alist[lt])
        lt += 1
    else :
        ans.append(blist[rt])
        rt += 1
while lt < n :
    ans.append(alist[lt])
    lt += 1
while rt < m :
    ans.append(blist[rt])
    rt += 1
for a in ans :
    print(a, end = ' ')
        