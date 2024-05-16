# 중요 - 얕은복사문제
n = int(input())
dp = list([0, []] for _ in range(n+1))
dp[1][0], dp[1][1] = 0, [1]

if n > 1:
  dp[2][0] = 1
  dp[2][1] = [1, 2]

#카운트, 포함인덱스 -> 이중dp
for i in range(3, n+1):
    a, b, c = float('inf'), float('inf'), float('inf')

    if i % 3 == 0:
        a = dp[i//3][0]
    if i % 2 == 0:
        b = dp[i//2][0]
    c = dp[i-1][0]
    if a <= b and a <= c:
        dp[i][0] = a + 1
        dp[i][1] = dp[i//3][1][:] # 얕은 복사 문제로 인해 슬라이싱 필요!!
        dp[i][1].append(i)
    elif b <= c and b <= a:
        dp[i][0] = b + 1
        dp[i][1] = dp[i//2][1][:]
        dp[i][1].append(i)
    elif c <= b and c <= a:
        dp[i][0] = c + 1
        dp[i][1] = dp[i-1][1][:]
        dp[i][1].append(i)
    
print(dp[-1][0])
print(*sorted(dp[-1][1], reverse=True))