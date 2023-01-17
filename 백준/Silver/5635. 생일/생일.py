import sys
input = sys.stdin.readline

number = int(input())
alist = list()
for _ in range(number) : 
    a, b, c, d = map(str, input().split())
    alist.append([a, int(b), int(c), int(d)])

# yyyy -> mm -> dd 
alist.sort(key = lambda x : x[1])
alist.sort(key = lambda x : x[2])
alist.sort(key = lambda x : x[3])

print(alist[number-1][0])
print(alist[0][0])
