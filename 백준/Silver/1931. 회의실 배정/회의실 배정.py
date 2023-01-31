#회의실 배정
import sys
input = sys.stdin.readline

n = int(input()) #회의의 수
time = []
for _ in range(n) :
    tmp1, tmp2 = map(int, input().split())
    time.append((tmp1, tmp2))
time.sort()
time.sort(key=lambda x:x[1])
'''
time[i][0] 튜플 앞 원소 
time[i][1] 튜플 뒷 원소 
'''
cnt = 1
end = time[0][1]
# print('time', time)
for i in range(1, n) :
    if time[i][0] >= end : 
        # print('time[i][1]', time[i][1])
        end = time[i][1] 
        cnt += 1 
print(cnt)
        