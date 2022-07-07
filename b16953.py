a, b = map(int, input().split())
count = 0

while True :
    if b % 10 == 1 :
       b = b // 10
       count += 1
    elif b % 2 == 0 :
       b = b // 2
       count += 1 
    
    if a == b :
        print(count+1)
        break
    elif (b % 2 != 0 and b % 10 != 1) or (a > b) :
        print(-1)
        break
    
