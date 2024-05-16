#최소cnt - bfs
#걷기: x-1 / x+1 (1초소요)
#순간이동: 2 * x (0초소요)
from collections import deque

def bfs():
    while q:
        x, time = q.popleft()
        if x == k:
            return time
        for nx in (2*x, x-1, x+1):
            if nx == 2*x:
                if 0 <= nx < 100001 and visited[nx] > time:
                    q.append([nx, time])
                    visited[nx] = time
            else:
                if 0 <= nx < 100001 and visited[nx] > time+1:
                    q.append([nx, time+1])
                    visited[nx] = time+1

n, k = map(int, input().split())
visited = [float('inf')] * 100001
visited[n] = 0
q = deque()
q.append([n, 0])
print(bfs())