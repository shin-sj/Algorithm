# 국회의원 선거
import sys
n = int(sys.stdin.readline().rstrip())
vote = list() #득표수
for i in range(0, n):
    vote.append(int(sys.stdin.readline().rstrip()))
answer = 0
m = max(vote)
# 기호 1번의 득표수가 다른 모든 사람의 득표수보다 많아질때까지 반복 
while m!=vote[0] or vote.count(m)>=2:
    # 기호 2번~N번 중에서 득표수가 가장 많은 후보자의 index찾기
    maxIndex = vote[1:].index(max(vote[1:]))+1
    # 기호 1번에 득표수 1 추가
    vote[0]+=1
    # 득표수가 가장 많았던 후보자의 득표수 1 감소
    vote[maxIndex]-=1
    # 다솜이가 매수한 사람 1 증가
    answer += 1
    m = max(vote)

print(answer)