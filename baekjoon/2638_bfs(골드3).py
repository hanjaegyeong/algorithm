#2638_bfs(골드3)
from collections import deque
dxdy = ((0,1),(1,0),(-1,0),(0,-1))

def bfs(): #bfs 인접2개 이하일때 delete추가
    q = deque([[0, 0]]) #바깥부분 돌면서 공기접촉시 처리
    while q:
        x, y = q.popleft()
        for i in dxdy:
            nx, ny = x + i[0], y + i[1]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] >= 1: #치즈면
                    graph[nx][ny] += 1 #공기접촉면 추가
                else: #치즈 아니면
                    visited[nx][ny] = 1 #방문하고!
                    q.append([nx, ny]) #다음칸에 넣기

graph = [] #graph에 카운팅***
ans = 0
n, m = map(int, input().split())

for i in range(n):
    graph.append(list(map(int, input().split())))

while True:
    visited = list([0] * (m) for _ in range(n))
    isend = 1
    bfs()
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3: #delete
                graph[i][j] = 0
                isend = 0
            elif graph[i][j] == 2: # +1만 된 경우엔 다시 1로 되돌려놓기
                graph[i][j] = 1
    if isend:
        print(ans)
        break
    ans += 1