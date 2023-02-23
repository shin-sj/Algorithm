import sys
from collections import Counter
input = sys.stdin.readline

n = int(input()) #준규가 가지고 있는 숫자카드의 개수
cards = []
for _ in range(n) :
    cards.append(int(input()))
cards.sort()
adict = Counter(cards).most_common(1)
print(adict[0][0])