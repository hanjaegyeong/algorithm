t = int(input())
dp = [0] * 12
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, 12):
    # 각 케이스에 +3, +2, +1 덧붙이는 경우
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range(t):
    n = int(input())
    print(dp[n])