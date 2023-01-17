#덩치
import sys
input = sys.stdin.readline

n = int(input())
alist = []
for _ in range(n) :
    x, y = map(int, input().split())
    alist.append((x,y))

for i in range(n) :
    cnt = 1
    for j in range(n) :
        if alist[i][0] < alist[j][0] and alist[i][1] < alist[j][1] :
            cnt += 1
    print(cnt, end=' ')