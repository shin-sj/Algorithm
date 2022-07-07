n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() #오름차순 
b.sort(reverse=True) #내림차순
result = 0

for i in range(n) : 
    result += a[i] * b[i]
    
print(result)