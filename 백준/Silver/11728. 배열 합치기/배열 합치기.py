import sys
input = sys.stdin.readline

n, m = map(int, input().split())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))
answer = []
aIdx, bIdx = 0, 0
# pointer을 이동시키면서 최대한 합치기
while aIdx < n and bIdx < m :
    if alist[aIdx] < blist[bIdx] :
        answer.append(alist[aIdx])
        aIdx += 1
    else :
        answer.append(blist[bIdx])
        bIdx += 1
# 남은 배열 합치기
# a 배열과 b 배열의 길이가 같지 않으면 1번의 과정이 끝난 뒤 남는 배열이 생길 수 있다.
while aIdx < n :
    answer.append(alist[aIdx])
    aIdx += 1
while bIdx < m :
    answer.append(blist[bIdx])
    bIdx += 1

for a in answer :
    print(a, end=' ')