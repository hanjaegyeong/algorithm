# bfs+오일러서킷(한붓그리기)
# 모든 노드의 연결 간선 수가 2의 배수개여야 함
# 덩어리 2개 이상이면 탈락

from collections import deque
dxdy = [(1,0), (-1,0), (0,1), (0,-1)]

# 오일러 체크 bfs
def check_euler(sx, sy):
    global result
    q = deque()
    q.append([sx, sy])
    visited[sx][sy] = 1    
    while q:
        x, y = q.popleft()
        for i in dxdy:
            cnt = 0
            nx, ny = x + i[0], y + i[1]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append([nx, ny])
                cnt += 1
        if cnt % 2 == 1: # 연결 간선 수 2의 배수 아니면
            result = 0 # 탈락

t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    result, mung_cnt = 1, 0
    visited = list([0] * m for _ in range(n))

    # 오일러 체크
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0 and not visited[i][j]:
                check_euler(i, j)
                mung_cnt += 1
    
    if mung_cnt >= 2: # 덩어리 두 개 이상이면
        result = 0 # 탈락

    print(result)