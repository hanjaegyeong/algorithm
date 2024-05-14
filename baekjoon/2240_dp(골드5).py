t, w = map(int, input().split()) #t초, 최대 w번
jadus = list(int(input()) for _ in range(t))

#이중리스트 - 시간i, 이동횟수j일 때 최대자두
dp = list(list([0] * (w+1)) for _ in range(t))
if jadus[0] == 1:
    dp[0][0] = 1
else:
    dp[0][1] = 1

#이동횟수 홀수인덱스:2, 짝수인덱스:1 위치
for i in range(1, t): #i번째
    for j in range(w+1): #j번 이동
        if j > i+1:
            continue
        if j == 0: #정지만 가능
            dp[i][j] = dp[i-1][j]
        elif j == i+1: #이전턴에 동일이동횟수 불가 - 이동만 가능
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) #유지/이동
        if jadus[i] == 1 and not j % 2: #홀
            dp[i][j] += 1
        elif jadus[i] == 2 and j % 2: #짝
             dp[i][j] += 1

print(max(dp[-1]))