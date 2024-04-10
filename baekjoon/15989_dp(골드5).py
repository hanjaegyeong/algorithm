t = int(input())
dp = [1] * 10001 #1만으로 나타내는 법

for i in range(2, 10001):
    dp[i] += dp[i-2] #1로 + 2하나 추가

for i in range(3, 10001):
    dp[i] += dp[i-3] #1,2로 + 3하나 추가

for _ in range(t):
    n = int(input())
    print(dp[n])