import heapq
import sys
input = sys.stdin.readline

def dijkstra(st, end, n): #st에서 출발하는 최단거리 찾기
    dist = [float('inf')] * (n+1) #가중치 리스트
    dist[st] = 0
    # 튜플로 초기세팅!
    q = [(0, st)] # st에서 st로 가는 경우 초기 삽입 (거리 0)
    while q:
        nowd, now = heapq.heappop(q)
        for nxt, nxtd in graph[now]: #연결 노드 탐색
            distsum = nxtd + nowd
            if distsum < dist[nxt]:
                dist[nxt] = distsum
                heapq.heappush(q, (distsum, nxt)) #튜플로 삽입!
    return dist[end]

n, m, x = map(int, input().rstrip().split())
graph = list([] for _ in range(m+1))

for i in range(m):
    s, e, t = map(int, input().rstrip().split())
    graph[s].append((e, t))

goans = [0] * (n+1)
comeans = [0] * (n+1)

for i in range(1, n+1):
    goans[i] += dijkstra(i, x, n) + dijkstra(x, i, n)

print(max(goans))