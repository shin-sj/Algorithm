#최단경로
import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split()) #v-정점의개수(1~v), e-간선의개수 
k = int(input()) #시작 정점의 번호
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1) # 최종 거리 배열 

# 간선 정보 입력 
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

def dijkstra(start) :
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist : 
            continue
        for weight, node in graph[now] :
            cost = weight + dist
            if cost < distance[node] :
                distance[node] = cost
                heapq.heappush(q, (cost, node)) 
                
dijkstra(k)
# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])