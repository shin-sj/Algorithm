import sys
input = sys.stdin.readline

n, m = map(int, input().split())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))
lt, rt = 0, 0
answer = []
while lt < n and rt < m:
    if alist[lt] < blist[rt] :
        answer.append(alist[lt])
        lt += 1
    else :
        answer.append(blist[rt])
        rt += 1
while lt < n :
    answer.append(alist[lt])
    lt += 1
while rt < m :
    answer.append(blist[rt])
    rt += 1
for a in answer:
    print(a, end = ' ')