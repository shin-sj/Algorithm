#문자열
import sys
input = sys.stdin.readline

a, b = input().split()
cnt = 0
ans = len(a)

for i in range(len(b)-len(a)+1) :
    cnt = 0
    for j in range(len(a)) :
        if a[j] != b[i+j] :
            cnt += 1
    ans = min(ans, cnt)
print(ans)
