import sys
input = sys.stdin.readline

n = int(input())
plist = list(map(int, input().split()))
plist.sort()
# print(plist)
sum = 0
for i in range(n) :
    for j in range(0, i+1) :
        sum += plist[j]
print(sum)