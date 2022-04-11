sList = list(map(int, input().split())) #리스트로 값 받음 
tList = list(map(int, input().split()))
S = 0
T = 0

for i in sList :
    S += i 
for i in tList :
    T += i 
    
if S >= T :
    print(S)
else :
    print(T)