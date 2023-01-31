import sys
from collections import Counter
input = sys.stdin.readline

N = int(input()) #준규가 가지고 있는 숫자카드의 개수 N
alist = []
for _ in range(N) :
    alist.append(int(input()))
alist.sort()
acount = Counter(alist).most_common(1)
print(acount[0][0])