# dfs는 시간초과!! n, m이 100 넘는다 싶으면 dp로 가야 함!!

n, m = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(n))
dp = list(list([0] * m)for _ in range(n))
dp[0][0] = graph[0][0]
dpLeft = list(list([0] * m)for _ in range(n))
dpRight = list(list([0] * m)for _ in range(n))

#첫줄. 왼->오
for i in range(1, m):
    dp[0][i] = dp[0][i-1] + graph[0][i]

# 각 행마다 왼->오, 오->왼 중 최적 dp값으로 갱신
for i in range(1, n):
    # 위->아래, 왼->오
    for j in range(m):
        toDown = dp[i-1][j] + graph[i][j]
        if j == 0:
            dpRight[i][j] = toDown
        else:
            dpRight[i][j] = max(toDown, dpRight[i][j-1] + graph[i][j])
    
    # 위->아래, 오->왼
    for j in range(m-1, -1, -1):
        toDown = dp[i-1][j] + graph[i][j]
        if j == m-1:
            dpLeft[i][j] = toDown
        else:
            dpLeft[i][j] = max(toDown, dpLeft[i][j+1] + graph[i][j])
    
    #두 DP 중 max값으로 dp 업데이트
    for j in range(m):
        dp[i][j] = max(dpLeft[i][j], dpRight[i][j])

print(dp[n-1][m-1])