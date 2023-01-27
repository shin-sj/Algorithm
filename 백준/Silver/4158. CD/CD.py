import sys
input = sys.stdin.readline

while True :
    n, m = map(int, input().split()) #n-상근이가 갖고 있는 cd수, m-선영이가 갖고 있는 cd수 
    nlist = [] #상근이가 갖고 있는 cd수 
    mlist = [] #선영이가 갖고 있는 cd수 
    if n == 0 and m == 0 :
        break
    for _ in range(n) :
        nlist.append(int(input())) #오름차순으로 주어짐
    for _ in range(m) :
        mlist.append(int(input()))
        
    ## 1. bruteforce ## 
    ''' input값이 매우 커서 완탐 불가능 -> 이분탐색이나 딕셔너리 사용 '''
    # cnt = 0
    # for nn in nlist :
    #     if nn in mlist :
    #         cnt += 1
    # print(cnt)
    
    ## 2. binary search ##
    cnt = 0
    for mm in mlist : 
        lt = 0
        rt = n - 1
        while lt <= rt :
            mid = (lt+rt)//2 
            if nlist[mid] == mm :
                cnt += 1
                break
            elif nlist[mid] > mm :
                rt = mid - 1
            elif nlist[mid] < mm :
                lt = mid + 1
    print(cnt)
                
    ##3. 딕셔너리 ##
    # ndict = {}
    # mdict = {}
    # cnt = 0
    # for _ in range(n) :
    #     ndict[int(input())] = 1
    # for _ in range(m) :
    #     tmp = int(input())
    #     if ndict.get(tmp) == 1 :
    #         cnt += 1
    # print(cnt)
