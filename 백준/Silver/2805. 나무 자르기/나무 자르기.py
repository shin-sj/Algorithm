import sys
input = sys.stdin.readline

n, m = map(int, input().split()) #n:나무의수, m:필요한 나무의 길이
trees = list(map(int, input().split())) #나무의 높이 
trees.sort() #이분탐색을 위해 오름차순 정렬 
lt = 0
rt = max(trees) 

while lt <= rt :
    mid = (lt+rt) // 2
    sum = 0 
    for t in trees : 
        if t > mid :
            sum += t-mid #잘린 나무 길이 계산 
    if sum < m : 
        rt = mid - 1
    else :
        lt = mid + 1

print(rt)