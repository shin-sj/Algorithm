import sys
input = sys.stdin.readline

n, l, d = map(int, input().split())
total_time = (n*l) + (n-1)*5
song_time = [False] * total_time

#노래 나오는 시간 - True
for i in range(0, total_time, l+5) :
    for j in range(i, l+i) :
        song_time[j] = True

for i in range(0, total_time, d) :
    if song_time[i] == False :
        print(i)
        break
else :
    print(i + d)