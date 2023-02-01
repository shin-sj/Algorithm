import sys
input = sys.stdin.readline
def binary_search(target, blist) :
    lt = 0
    rt = len(blist) - 1 
    result = -1
    while lt <= rt :
        mid = (rt + lt) // 2 #인덱스! 
        if target > blist[mid] :
            result = mid
            lt = mid + 1
        else : 
            rt = mid - 1
    return result  
    
tc = int(input())
for _ in range(tc) :
    n, m = map(int, input().split())
    alist = list(map(int, input().split()))
    blist = list(map(int, input().split()))
    alist.sort()
    blist.sort()
    ans = 0
    for a in alist :
        ans += binary_search(a, blist) + 1
    print(ans)