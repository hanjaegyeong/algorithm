#두 개의 큐 한 번에 이동
from collections import deque
import sys
input = sys.stdin.readline
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs():
    while jq:
        for _ in range(len(fq)): # 불들 한 칸 확장
            x, y, cnt = fq.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < r and 0 <= ny < c and (graph[nx][ny] == '.' or graph[nx][ny] == 'J'):
                    fq.append([nx, ny, cnt + 1])
                    graph[nx][ny] = 'F'

        for _ in range(len(jq)): # 지훈이 한 칸 이동
            x, y, cnt = jq.popleft()
            if x == r - 1 or y == c - 1 or x == 0 or y == 0:
                return cnt
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and graph[nx][ny] == '.':
                    visited[nx][ny] = 1
                    jq.append([nx, ny, cnt + 1])


    return "IMPOSSIBLE"

r, c = map(int, input().rstrip().split())
graph = list(list(input().rstrip()) for _ in range(r))
visited = list(([0] * c) for _ in range(r))
result = 0

fq = deque()
jq = deque()

# 큐 채우기
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'J':
            jq.append([i, j, 1])
            visited[i][j] = 1
        elif graph[i][j] == 'F':
            fq.append([i, j, 1])

print(bfs())