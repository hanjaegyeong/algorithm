#중요
#가장 긴 증가하는 부분 수열 -> dp
#2중 for문 이용!! - 한 점 잡고 돌리기 메모

n = int(input())
a = list(map(int, input().split()))

dp = [1] * n

# max로 갱신
for i in range(n):
    for j in range(i+1, n):
        if a[j] > a[i]:
            dp[j] = max(dp[j], dp[i]+1)

print(max(dp))