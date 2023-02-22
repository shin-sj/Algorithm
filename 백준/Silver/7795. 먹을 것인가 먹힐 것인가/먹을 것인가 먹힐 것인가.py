#먹을 것인가 먹힐 것인가. 
import sys
input = sys.stdin.readline

tc = int(input()) #테스트케이스
for _ in range(tc) :
    n, m = map(int, input().split())
    alist = list(map(int, input().split()))
    blist = list(map(int, input().split()))
    alist.sort()
    blist.sort()
    cnt = 0

    for a in alist :
        lt = 0
        rt = len(blist) - 1
        result = -1
        
        while lt <= rt :
            mid = (rt+lt) // 2  #index
            if blist[mid] < a :
                result = mid 
                lt = mid + 1
            else :
                rt = mid - 1
        cnt += result + 1
    print(cnt)
