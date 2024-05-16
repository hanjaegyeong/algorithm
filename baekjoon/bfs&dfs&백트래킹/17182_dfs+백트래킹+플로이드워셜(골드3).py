#17182_dfs+백트래킹+플로이드워셜(골드3)

#dfs로 백트래킹. 최단비용으로 모든 행성 탐사 min값 ans 갱신***
def dfs(now, cnt, cost): #현재위치, cnt, cost갱신
    global result
    if cnt == n:
        result = min(result, cost) #끝까지 도달한 경우들 min값 갱신***
        return
    for nxt in range(n):
        if not visited[nxt]:
            visited[nxt] = 1
            dfs(nxt, cnt+1, cost+graph[now][nxt]) #현재위치에서 next위치로 가는 비용 갱신
            visited[nxt] = 0 #백트래킹

n, k = map(int, input().split()) #행성개수, 위치
graph = list(list(map(int,input().split())) for _ in range(n))
visited = [0]*n
visited[k] = 1
result = 10**8
       
#플루이드 워셜 모든 값 graph에 갱신
#i에서 j로 가는 최단거리
for i in range(n):
    for j in range(n):
        for z in range(n):
            graph[i][j] = min(graph[i][j], graph[i][z] + graph[z][j])

dfs(k, 1, 0)
print(result)