import sys
input = sys.stdin.readline

n = int(input()) #배열의 크기 
nlist = list()
for _ in range(n) :
    nlist.append(int(input()))
nlist.sort()
tmp = list()
for i in range(n) :
    cnt = 0
    for j in range(nlist[i], nlist[i] + 5) :
        if j not in nlist :
            cnt += 1
    tmp.append(cnt)
print(min(tmp))