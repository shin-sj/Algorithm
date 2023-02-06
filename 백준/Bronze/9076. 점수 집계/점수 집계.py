import sys
input = sys.stdin.readline

tc = int(input()) #테스트케이스의 개수
for _ in range(tc) :
    nlist = list(map(int, input().split())) #다섯 심판이 준 점수 다섯 개의 정수
    nlist.sort()
    del nlist[0] #최저점 삭제
    del nlist[-1] #최고점 삭제
    if nlist[-1] - nlist[0] >= 4 :
        print("KIN")
    else :
        print(sum(nlist))
    