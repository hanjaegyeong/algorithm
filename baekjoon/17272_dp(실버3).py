# re풀기
n = int(input())
dp = [0] * (n)
dp[0] = 1

if n > 1:
    dp[1] = 3

# 세로짜리 두개 들어가는 중복 경우 제외
# dp[i-2] * 3이 아니라 2를 곱해야 함
for i in range(2, n):
    dp[i] = (dp[i-1] + dp[i-2] * 2) % 10007

print(dp[-1])