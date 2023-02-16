import sys
input = sys.stdin.readline

n, m = map(int, input().split()) #n-카드의 개수, m-합체 수 
card = list(map(int, input().split()))
#만들 수 있는 가장 작은 점수는?
for _ in range(m) :
    card.sort()
    tmp = card[0] + card[1]
    card[0] = tmp
    card[1] = tmp
# print(card)
print(sum(card))