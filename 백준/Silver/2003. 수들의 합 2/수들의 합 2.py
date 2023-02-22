import sys
input = sys.stdin.readline

n, m = map(int, input().split()) 
alist = list(map(int, input().split()))
#i~j의 합이 m이 되는 경우의 수 구하기 
start = 0
end = 0
ans = 0
while start <= end and end <= n :
    if sum(alist[start:end]) == m :
        ans += 1
        start += 1
    elif sum(alist[start:end]) < m :
        end += 1
    else :
        start += 1
print(ans)