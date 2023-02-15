import sys
input = sys.stdin.readline

w, h = map(int, input().split()) #가로, 세로
w_len = [0, w]
h_len = [0, h]

for _ in range(int(input())) :
    xy, length = map(int, input().split())
    if xy == 0 :
        h_len.append(length)
    else :
        w_len.append(length)
w_len.sort()
h_len.sort()
maxSquare = 0
# print(w_len, h_len)
for i in range(1, len(w_len)) :
    for j in range(1, len(h_len)) :
        width = w_len[i] - w_len[i-1]
        height = h_len[j] - h_len[j-1]
        maxSquare = max(maxSquare, width*height)
print(maxSquare)