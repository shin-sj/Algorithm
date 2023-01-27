import sys
from collections import deque
input = sys.stdin.readline
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def bfs(sx, sy) :
    dQ = deque()
    dQ.append((sx,sy))
    visited[sx][sy] = 1 #시작위치 방문 표시
    cnt = 1 #시작위치 개수 세기 
    while dQ : 
        x, y = dQ.popleft()
        zeros[x][y] = group #현재 그룹에 포함 
        for i in range(4) :
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<n and 0<=yy<m :
                if visited[xx][yy] :
                    continue
                #이동할 위치가 빈 곳이라면 
                if board[xx][yy] == 0 : 
                    dQ.append((xx, yy))
                    visited[xx][yy] = 1
                    cnt += 1
    return cnt
#이동할 수 있는 총 그룹의 개수를 세는 함수 
def move_count(x, y) : 
    data = set() #그룹 번호를 담기 위한 집합 데이터 생성(중복 제거를 위해 set사용)
    for i in range(4) :
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<n and 0<=yy<m :
            if zeros[xx][yy] != 0 :
                data.add(zeros[xx][yy])
    cnt = 1 #현재 x, y위치 세기
    for c in data : 
        #딕셔너리에 추가
        cnt += info[c]
        cnt %= 10
    return cnt  #출력값 반환


n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
zeros = [[0] * m for _ in range(n)]
answer = [[0] * m for _ in range(n)] #정답 배열 
group = 1 # 1번 그룹 생성
info = {} # (그룹명:개수)딕셔너리

for i in range(n) :
    for j in range(m) :
        if board[i][j] == 0 and visited[i][j] == 0 :
            cnt = bfs(i, j)
            info[group] = cnt #딕셔너리에 그룹명과 개수 추가 
            group += 1 #다음 그룹 
            
#전체 데이터를 하나씩 살펴보며
for i in range(n) :
    for j in range(m) :
        #벽이 있다면 
        if board[i][j] :
            answer[i][j] = move_count(i, j)
            
for i in range(n) :
    print("".join(map(str, answer[i])))