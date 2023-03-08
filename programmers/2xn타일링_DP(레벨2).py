#DP. 메모할 것: 채우는 방법 수
def solution(n):
    dp = [0] * 60001 #i번째 칸 채우는 방법 수
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        # i-1에서 세로 하나 추가 or i-2에서 가로 두개 추가
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    return dp[n]