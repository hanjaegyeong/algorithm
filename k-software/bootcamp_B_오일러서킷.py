#dfs_오일러서킷(한붓그리기)

import sys
sys.setrecursionlimit(10**9)
dxdy = [(1,0), (-1,0), (0,1), (0,-1)]

#간선 채우기 bfs
def check_edge(x, y):
    global nothing
    for i in dxdy:
        nx, ny = x + i[0], y + i[1]
        if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
            edges[node_num[x][y]][node_num[nx][ny]] = 1
            #i에서 j인덱스 가는 간선 있음

#오일러서킷 dfs
def euler_dfs(now):
    for i in graph[now]:
        if edges[now][i]:
            edges[now][i]-=1
            edges[i][now]-=1
            euler_dfs(i)
    return(1)

t = int(input())
for _ in range(t):
    isover = 0
    m, n = map(int, input().split())
    matrix, graph, node_num, edges = [], {}, [], list([0] * (n*m) for _ in range(n*m))

    for i in range(n):
        nums = []
        for j in range(m):
            nums.append(i*m + j)
        node_num.append(nums)
    
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                check_edge(i, j)
    
    for i in range(n*m):
        graph[i]=[]
        rowSum=0
        for j in range(n*m):
            for k in range(edges[i][j]):
                rowSum+=1
                graph[i].append(j)
        if rowSum%2==1: #연결 간선 2의 배수 아니면
            isover = 1 #탈락

    if isover == 1:
        print(0)
        continue

    print(euler_dfs(0))