import sys
input = sys.stdin.readline

def binary_search(target, blist):
    lt = 0 #시작 
    rt = len(blist)-1 #인덱스로 계산할 것이기 때문. 
    result = -1 # -1이어야 하는 이유? 개수를 구해야 하기 때문에 인덱스 +1을 해줘야 한다, 그러나 blist에 target보다 작은 수가 없을 경우에는 계속해서 +1이 되어 버림. 따라서 -1 + 1 = 0이기 위해 초기값을 -1로 두는 것. 

    while lt <= rt: 
        mid = (lt + rt) // 2 #index 
        if blist[mid] < target :
            result = mid
            lt = mid + 1
        else:
            rt = mid -1
    return result

tc = int(input())
for _ in range(tc):
    N, M = map(int, input().split())
    alist = list(map(int, input().split()))
    blist = list(map(int, input().split()))
    alist.sort()
    blist.sort()
    cnt = 0 
    for i in alist :
        cnt += binary_search(i, blist) + 1

    print(cnt)