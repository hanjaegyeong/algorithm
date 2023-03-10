# 가장 큰 컨소시엄_플로이드워셜
# a->b && b->c == a->c
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split()) # n: 기업 수, m: 관계 수
    ans = 0
    graph = list([0] * (n+1) for _ in range(n+1)) # graph[i][j] == 1: i번 기업은 j번 기업과 연결되어 있음
    
    for _ in range(m):
        a, b = map(int, input().split()) # 관계 양방향
        graph[a][b] = 1
        graph[b][a] = 1

    # i->j && j->k == i->k
    # j 경유할 때, i 출발 k 도착
    for j in range(n+1):
        for i in range(n+1):
            for k in range(n+1):
                if graph[i][j] == 1 and graph[j][k] == 1:
                    graph[i][k] = 1
    
    for i in range(n+1):
        ans = max(graph[i].count(1), ans)
    
    print(ans)