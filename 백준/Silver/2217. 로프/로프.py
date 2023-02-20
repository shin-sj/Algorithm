import sys
input = sys.stdin.readline

N = int(input()) #로프의 개수 
alist = [] #중량 list
for _ in range(N) :
    weight = int(input())
    alist.append(weight)
alist.sort(reverse=True)
# print(alist)
answer = 0
tmp = 0
for i in range(len(alist)) :
    tmp = alist[i] * (i+1)
    answer = max(answer, tmp)
print(answer)