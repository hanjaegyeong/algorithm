#10159_플로이드워셜
#비교 불가능한 물건 개수
#플로이드워셜 True/False(거리가중치값 안주어진 문제이므로)
#a->b, b->a 불가능하면 cnt+=1
import sys
input = sys.stdin.readline

n = int(input()) #물건개수
m = int(input()) #물건쌍
graph = list([0] * n for _ in range(n))

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1 #1로 표시! true/false

#플로이드워셜 i->j & j->k = i->k
#가장 바깥쪽 for문은 경유할 정점,가운데 for문은 출발 정점,가장 안쪽 for문은 도착 정점***
for j in range(n):
    for i in range(n):
        for k in range(n):
            if graph[i][j] and graph[j][k]:
                graph[i][k] = 1

for i in range(n):
    cnt = 0
    for j in range(n):
        if not graph[i][j] and not graph[j][i]: #i->j, j->i 없으면
            cnt += 1
    print(cnt-1)