#2206_bfs(골드3)
#3차원 visited [x][y][벽뚫유무]에 cnt 담아서 +1

import sys
from collections import deque
input = sys.stdin.readline
dxdy = [(1,0),(-1,0),(0,-1),(0,1)]

def bfs():
    while q:
        x, y, z = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][z]
        for i in range(4):
            nx, ny = x + dxdy[i][0], y + dxdy[i][1]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == "1" and z == 0 :
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append((nx, ny, 1))
                # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 곳이면
                elif graph[nx][ny] == "0" and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append((nx, ny, z))
    return -1

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))
visited = list(list([0]*2 for _ in range(m)) for _ in range(n))
visited[0][0][0] = 1
q = deque()
q.append((0, 0, 0))
print(bfs())