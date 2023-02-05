#영수증
import sys
input = sys.stdin.readline

x = int(input()) #총 금액
n = int(input()) #구매한 물건의 종류의 수 
price = 0
for _ in range(n) :
    a, b = map(int, input().split()) #각 물건의 가격 a와 개수b
    price += (a * b)

if price == x :
    print("Yes")
else :
    print("No")