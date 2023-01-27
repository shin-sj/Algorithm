#딸기 -> 초코 -> 바나나 
n = int(input()) #우유 가게의 수
milk = list(map(int, input().split()))
cnt = 0
flag = 0
for i in range(len(milk)) :
    flag %= 3 
    if milk[i] == flag :
        cnt += 1
        flag += 1
print(cnt)