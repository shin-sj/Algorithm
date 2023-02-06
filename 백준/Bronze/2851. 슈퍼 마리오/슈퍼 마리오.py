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

# ans,score = 0,0
# for i in range(10):
#     score+=int(input())
#     if 100-ans >= abs(100-score): # = 을 넣어야 절댓값이 같을 시 최대 총점 출력이 가능
#         ans = score
# print(ans)
