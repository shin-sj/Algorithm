#집합의 표현
#union-find알고리즘
import sys
sys.setrecursionlimit(1000000) # 재귀 깊이 제한 늘리기
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)] # 자기 자신을 부모로 갖는 n + 1개 집합
# 찾기 연산 ( 같은 집합에 속하는지 확인하기 위한 함수 )
def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]
# 합집합 연산 ( 두 집합을 합치기 위한 함수 )
def union(a, b) :
    a = find(a)
    b = find(b) 
    if a<b :
        parent[b] = a
    else :
        parent[a] = b
        
for _ in range(m) :
    c, a, b = map(int, input().split())
    if c == 0 :
        union(a, b)
    else : #c==1
        if find(a) == find(b) :
            print('YES')
        else :
            print('NO')
        