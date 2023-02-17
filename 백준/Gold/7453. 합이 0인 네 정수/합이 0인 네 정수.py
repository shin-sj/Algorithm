n = int(input())

result = 0
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ab = dict()
#a,b따로 c,d따로 계산 
for a in A:
    for b in B:
        v = a + b
        if v not in ab.keys():
            ab[v] = 1
        else:
            ab[v] += 1
for c in C:
    for d in D:
        v = -1 * (c + d)
        if v in ab.keys():
            result += ab[v]

print(result)