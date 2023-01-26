import sys
input = sys.stdin.readline

n = int(input()) # 1,000보다 작거나 같은 자연수 N
count = 0
for i in range(1, n+1) :
    number = list(map(int, str(i)))
    if i < 100 : #100보다 작으면 모두 한수이다. 
        count += 1
    elif number[0]-number[1] == number[1]-number[2] :
        count+= 1
print(count)