n = int(input())
num = n
ans = 0

while True :
    a = num // 10 
    b = num % 10
    c = (a+b) % 10
    num = (b*10) + c 
    
    ans += 1
    if num == n :
        break
print(ans) 