#A번 BFS풀이 
from collections import deque

def bfs(x):
    global cnt
    cnt = 1
    q = deque()
    q.append(graph[x])
    while q:
        next = q.popleft()
        for i in range(len(next)):
            nx = next[i]
            if not visited[nx]:
                cnt += 1
                visited[nx] = cnt
                q.append(graph[nx])

t = int(input())
for _ in range(t):
    n, m = map(int, input().split()) #노드 수, 간선 수
    ans = 0
    graph = list([] for _ in range(n+1))
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    for i in range(1, n+1):
        visited = [0] * (n+1)
        visited[i] = 1
        bfs(i)
        ans = max(ans, max(visited))
    print(ans)