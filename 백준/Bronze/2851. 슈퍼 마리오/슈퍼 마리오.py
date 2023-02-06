import sys
input = sys.stdin.readline

sumlist = [] #더한 값 list
sum = 0
for _ in range(10) :
    sum += int(input()) 
    sumlist.append(sum)
# print(sumlist)
minnum = (100-sumlist[0], 0)
for i in range(10) :
    if abs(100 - sumlist[i]) <= minnum[0] : 
        minnum = (100-sumlist[i], i)
print(sumlist[minnum[1]])