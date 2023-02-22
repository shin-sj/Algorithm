#먹을 것인가 먹힐 것인가. 
import sys
input = sys.stdin.readline

tc = int(input()) #테스트케이스
for _ in range(tc) :
    n, m = map(int, input().split())
    alist = list(map(int, input().split()))
    blist = list(map(int, input().split()))
    alist.sort(reverse=True)
    blist.sort(reverse=True)
    ans = 0
    aIdx = 0
    bIdx = 0 
    
    while aIdx < n and bIdx < m :
        if alist[aIdx] > blist[bIdx] :
            ans += m - bIdx 
            aIdx += 1
        else :
            bIdx += 1
            
    print(ans)