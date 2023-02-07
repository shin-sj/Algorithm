import sys
input = sys.stdin.readline

N, L, D = map(int, input().split())
total = N * L + (N - 1) * 5 # 앨범의 총 길이
song_time = [False] * total #노래 나오는 시간 체크 

for i in range(0, total, L + 5): # 각 노래는 0 초부터 시작해서 L + 5 초마다 나온다.
    for j in range(i, i + L): # 시작하는 부분 i부터 노래가 끝나는 부분인 i + L 전까지 체크
        song_time[j] = True
        
for i in range(0, total, D): # 0초부터 D초마다 노래가 나오는지 체크
    if song_time[i] == False:
        print(i)
        break
else:
    print(i + D)