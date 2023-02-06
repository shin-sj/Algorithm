import sys
input = sys.stdin.readline

A, B, C, M = map(int, input().split()) 
#A : 1시간 일했을때 쌓이는 피로도
#B : 1시간 일했을때 처리할 수 있는 일
#C : 1시간 쉬었을때 줄어드는 피로도
#M : M넘지 않게 일할수 있음
tired = 0 #피로도 계산 
work = 0 #일 계산 
#하루에 최대 얼마나 일을 할 수 있는지 ?? 

for i in range(24) :
    tired_tmp = tired + A
    if tired_tmp > M :
        tmp = tired - C 
        if tmp < 0 :
            tired = 0
        else :
            tired = tmp
        continue
    tired += A
    work += B
        
print(work)