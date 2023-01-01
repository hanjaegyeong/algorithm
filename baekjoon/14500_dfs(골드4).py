#14500_dfs(골드4)
#ㅏ, ㅗ 모양 처리하기 주의
import sys
sys.setrecursionlimit(10**8)
dxdy = ((-1, 0),(1,0),(0,-1),(0,1))

def dfs(x, y, cnt, s):
    global ans
    if cnt >= 4:
        ans = max(ans, s) #ans 갱신
        return
    for i in dxdy:
        nx, ny = x + i[0], y + i[1]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            #여기서 ㅓ, ㅗ모양 처리하기***
            if cnt == 2: #3번째(nx,ny) 포함시키고 2번째(x,y)(중앙자리)로 다시
                visited[nx][ny] = 1
                dfs(x, y, cnt + 1, s + graph[nx][ny])
                visited[nx][ny] = 0
            
            visited[nx][ny] = 1
            dfs(nx, ny, cnt + 1, s + graph[nx][ny])
            visited[nx][ny] = 0

n, m = map(int, input().split())
graph = []
ans = 0
visited = list([0] * (m) for _ in range(n))
for _ in range(n):
    graph.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 1, graph[i][j])
        visited[i][j] = 0
print(ans)