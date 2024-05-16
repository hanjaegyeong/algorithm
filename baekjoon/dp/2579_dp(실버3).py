# 연속해서 밟은 여부도 메모 필요 -> 이중리스트!!

n = int(input())
cost = list(int(input()) for _ in range(n))
dp = list([0] * 2 for _ in range(n))
dp[0][0] = cost[0]
if n > 1:
    dp[1][0], dp[1][1] = cost[1], cost[0] + cost[1]

for i in range(2, n):
    dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + cost[i] #한 칸 띄고 밟는 경우
    dp[i][1] = dp[i-1][0] + cost[i] #바로 밟는 경우

print(max(dp[n-1]))