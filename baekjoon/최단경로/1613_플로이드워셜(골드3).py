#1613_플로이드워셜(골드3)
#pypy3로 제출
#플로이드워셜 a->b b->c : a->c

import sys
input = sys.stdin.readline

n, k = map(int, input().split()) #사건개수n
graph = [[0] * n for _ in range(n)]
seek = []

for _ in range(k):
    a, b = map(int, input().split()) #a가 b보다 먼저
    graph[a-1][b-1] = 1

s = int(input()) #구할 관계
for _ in range(s):
    a, b = map(int, input().split())
    seek.append([a-1, b-1])

#경유, 출발, 도착
for j in range(n):
    for i in range(n):
        for k in range(n):
            if graph[i][j] and graph[j][k]:
                graph[i][k] = 1

for a, b in seek:
    if graph[a][b]:
        print(-1)
    elif graph[b][a]:
        print(1)
    else:
        print(0)