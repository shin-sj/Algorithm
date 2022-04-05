import math

d, h, w = map(int, input().split())
k = (d**2) / ((h**2)+(w**2))
sol = math.sqrt(k)

print(math.trunc(h*sol), math.trunc(w*sol))