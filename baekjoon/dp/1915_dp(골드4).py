# 브루트포스 불가-> 최대 (1000 ** 2) ** 2 되기 때문
# dp

n, m = map(int, input().split())
graph = list(list(int(i) for i in input()) for _ in range(n))
dp = list(list([0] * m) for _ in range(n))
result = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0: #0일 때
            continue
        else: #1일 때
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

for i in dp:
    result = max(result, max(i))

print(result ** 2)