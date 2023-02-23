# 수열 - 누적합
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
alist = list(map(int, input().split()))

part_sum = sum(alist[:k])
result = []
result.append(part_sum)

for i in range(0, len(alist)-k):
    part_sum = part_sum - alist[i] + alist[i+k]
    result.append(part_sum)

print(max(result))