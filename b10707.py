A = int(input())
B = int(input())
C = int(input())
D = int(input())
joi = int(input())

xPrice = A * joi 

if C < joi : 
    yPrice = B + (joi-C)*D 
else :
    yPrice = B
    
if xPrice < yPrice :
    print(xPrice)
else :
    print(yPrice)