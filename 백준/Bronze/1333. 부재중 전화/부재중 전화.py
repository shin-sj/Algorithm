#부재중 전화
import sys
input = sys.stdin.readline

N, L, D = map(int, input().split())
#N - 노래의 개수
#L - 노래의 길이
#D - 전화벨은 D초에 한번씩 울린다. 
total = (N*L) + (N-1)*5
board = [0] * total 

for i in range(0, total, L+5) :
    for j in range(i, i+L) :
        board[j] = 1 #노래 나오는 시간 체크
for i in range(0, total, D) :
    if board[i] == 0 :
        print(i)
        break
else :
    print(i+D)