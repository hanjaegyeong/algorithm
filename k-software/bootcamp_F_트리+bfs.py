#트리+bfs_두 노드 사이의 거리
#몇명거쳐서 연결되는지(직접연락은 1), 안되면 "No" 출력
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def bfs(a, b):
    q = deque()
    for i in graph[a]:
        q.append([i, 1]) #연결노드, cnt
    while q:
        x, cnt = q.popleft()
        if x == b:
            print(cnt)
            return
        for i in graph[x]:
            nx = i
            if not visited[x][nx]: #x에서 nx가는 경우 없으면
                visited[x][nx] = cnt + 1
                q.append([nx, cnt+1])
    print("No")
    return

for _ in range(t):
    n = int(input()) #총 가입자 수
    graph = [0]
    visited = list([0] * (n+1) for _ in range(n+1))
    for i in range(1, n+1): #i번째 사람과 연결된 사람들
        tmp, *relations = list(map(int, input().split()))
        graph.append(relations)

    a, b = map(int, input().split()) #a, b가 몇명거쳐서 연결되는지
    bfs(a, b)
