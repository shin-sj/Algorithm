n = int(input())

data = []
for i in range(n):
    data.append(int(input()))
    
result = 0

for i in range(n-2, -1, -1): 
    if data[i] >= data[i+1] : 
        result += data[i] - data[i+1] +1
        data[i] = data[i+1] - 1

print(result)