# 1. Bruteforce 
import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split()) #n=도시의 크기, m-선택할 치킨가게 수
board = [list(map(int, input().split())) for _ in range(n)] #도시의 정보
#0-빈칸, 1-집, 2-치킨집
ans = 999999
home = []
chicken = []
for i in range(n) :
    for j in range(n) : 
        if board[i][j] == 1 :
            home.append([i, j])
        elif board[i][j] == 2 :
            chicken.append([i, j])
# print(chicken)
# chicken 배열에서 m개 선택
for chi in combinations(chicken, m) :
    tmp = 0
    for h in home :
        chi_len = 999 
        for j in range(m) :
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        tmp += chi_len
    ans = min(ans, tmp)
print(ans)