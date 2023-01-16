#기타줄
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) #n: 필요한 개수, m:브랜드 종류
price =[]

for i in range(m) :
    a, b = map(int, input().split())
    price.append((a,b))
# print(price)
price.sort(key = lambda x : x[1])
one_price = price[0][1] #낱개 가격이 젤 싼것
price.sort()
pack_price = price[0][0] #패키지 가격이 젤 싼것 

# 낱개로 전부 구매. 
answer = one_price * n 

# 패키지로 전부 구매.
if n % 6 == 0 : #딱 떨어짐
    tmp = n // 6 
else :
    tmp = (n//6) + 1
answer = min(answer, pack_price * tmp)

# 패키지 + 낱개 구매. 
tmp = n // 6 
tmp2 = n % 6
answer = min(answer, (tmp*pack_price)+(tmp2*one_price))

print(answer)