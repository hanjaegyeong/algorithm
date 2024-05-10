# 인접한 집들끼리 색 다름

n = int(input())
#i번째 집 각각 rgb로 칠하는 경우
cost = list(list(map(int, input().split())) for _ in range(n))

# dp[i][j] i번째집 j로 칠하는 비용 최솟값
# dp[i][0], dp[i][1], dp[i][2] 세 개 따로 메모하면서 진행
dp = list([0] * 3 for _ in range(n))
dp[0][0], dp[0][1], dp[0][2] = cost[0][0], cost[0][1], cost[0][2]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

print(min(dp[n-1]))