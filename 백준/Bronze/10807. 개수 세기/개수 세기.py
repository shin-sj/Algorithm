n = int(input())
alist = list(map(int, input().split()))
key = int(input())
cnt = 0
for a in alist :
    if a == key :
        cnt += 1
print(cnt)