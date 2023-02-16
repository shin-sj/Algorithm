import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split()) #n-각 줄의 칸 수, k-반대편 줄로 이동할 때 k칸 더 앞으로 이동
board = [list(map(int, input().rstrip())) for _ in range(2)] #왼쪽줄, 오른쪽줄 순서
visited = [([0] * n) for _ in range(2)]
dQ = deque()
visited[0][0] = 1 #거리수는 계산 안하고, 방문여부만 체크 
dQ.append((0,0)) #각 유저는 항상 왼쪽 줄의 1번 칸 위에 서 있다. 
time = -1
flag = False
while dQ :
    for _ in range(len(dQ)) :
        x, y = dQ.popleft()
        if y+1 >= n or y+k >= n:
            flag = True #클리어 가능 
            break
        #한칸 앞으로 이동
        if visited[x][y+1] == 0 and board[x][y+1] == 1 :
            visited[x][y+1] = 1
            dQ.append((x, y+1))
        #한칸 뒤로 이동
        if y-1 > time + 1 and visited[x][y-1] == 0 and board[x][y-1] == 1 :
            visited[x][y-1] = 1
            dQ.append((x, y-1))
        #반대편 줄로 점프 
        if visited[0][y+k] == 0 and board[(x+1) % 2][y+k] == 1:
            visited[(x+1)%2][y+k] = 1
            dQ.append(((x+1)%2, y+k))
    time += 1
print(1) if flag else print(0)