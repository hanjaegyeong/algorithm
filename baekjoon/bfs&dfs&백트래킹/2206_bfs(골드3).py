# 2206_bfs(골드3)
from collections import deque

dxdy = [(1,0),(-1,0),(0,-1),(0,1)]

def bfs():
    while q:
        x, y, z, cnt = q.popleft()
        if x == n-1 and y == m-1:
            return cnt
        for i in range(4):
            nx, ny = x + dxdy[i][0], y + dxdy[i][1]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][z]:
                if graph[nx][ny] == "0": #벽 아닐때
                    visited[nx][ny][z] = 1 #가기
                    q.append([nx, ny, z, cnt+1])
                else: #벽일 때
                    if z == 0: #뚫은적 없으면
                        visited[nx][ny][z] = 1 #벽뚫고가기
                        q.append([nx, ny, 1, cnt+1])
    return -1

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))
visited = list(list([0]*2 for _ in range(m)) for _ in range(n))
visited[0][0][0] = 1
q = deque()
q.append([0, 0, 0, 1])
print(bfs())