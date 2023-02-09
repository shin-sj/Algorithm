import sys
from collections import deque

def bfs(x):
    # +1, -1, +a, -a, +b, -b, *a, *b칸 이동
    dy = [1, -1, a, -a, b, -b, a, b]
    queue = deque([x])
    visited[x] = True
    while queue:

        # 현재 위치 확인
        target = queue.popleft()

        # 현재 위치에서 총 8가지 경우의 수를 bfs 탐색으로 수행
        for i in range(8):
            # 6가지 경우는 + 연산
            if i < 6:
                y = target + dy[i]
                # 현재 위치와 이동하는 수를 더한 값이 돌다리 위에 있고 탐색하지 않았다면
                # 큐에 추가하고 그때의 턴을 +1 해준다.
                if 0 <= y <= 100000 and visited[y] == False:
                    queue.append(y)
                    visited[y] = True
                    graph[y] = graph[target] + 1
            # 나머지 2개의 경우는 배수이기 때문에 곱하기로 연산
            else:
                y = target * dy[i]
                # 현재 위치와 이동하는 수를 곱한 값이 돌다리 위에 있고 탐색하지 않았다면
                # 큐에 추가하고 그때의 턴을 +1 해준다.
                if 0 <= y <= 100000 and visited[y] == False:
                    queue.append(y)
                    visited[y] = True
                    graph[y] = graph[target] + 1


a, b, n, m = map(int, sys.stdin.readline().split())
graph = [0 for _ in range(100001)]
visited = [False for _ in range(100001)]
bfs(n)
print(graph[m])