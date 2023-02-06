ans,score = 0,0
for i in range(10):
    score+=int(input())
    if 100-ans >= abs(100-score): # = 을 넣어야 절댓값이 같을 시 최대 총점 출력이 가능
        ans = score
print(ans)