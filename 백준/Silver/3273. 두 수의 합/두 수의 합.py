import sys
input = sys.stdin.readline

n = int(input())
alist = list(map(int, input().split()))
alist.sort()
x = int(input())
start,end = 0,n-1
ans = 0

while start < end :
    if alist[start] + alist[end] == x :
        ans += 1
        start += 1
    elif alist[start] + alist[end] < x :
        start += 1
    else :
        end -= 1

print(ans)