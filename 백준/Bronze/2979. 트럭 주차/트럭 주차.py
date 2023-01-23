import sys
input = sys.stdin.readline

a, b, c = map(int, input().split()) #주차요금 a,b,c
startTime = []
endTime = []

for _ in range(3) :
    tmp1, tmp2 = map(int, input().split())
    startTime.append(tmp1)
    endTime.append(tmp2)

data = [0] * 100 
for i in range(3) :
    for j in range(startTime[i], endTime[i]) : 
        data[j] += 1 

ans = 0
for d in data :
    if d == 1 :
        ans += a
    if d == 2 :
        ans += (b*2)
    if d == 3 :
        ans += (c*3)
print(ans)