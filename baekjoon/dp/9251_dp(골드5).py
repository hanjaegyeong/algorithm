# re풀기
# 같은 열/행이면 한 번 같으면 +1 후 쭉 해당 수 유지
# 2중 for문
# C까지 - 0 1 1 1 1 1
# A까지 - 1 1 2 2 2 2
# P까지 - 1 1 2 2 2 3

a = list(input())
b = list(input())
dp = list(list([0] * (len(b)+1)) for _ in range(len(a)+1))
result = 0

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

for i in dp:
    for j in i:
        if j > result:
            result = j

print(result)