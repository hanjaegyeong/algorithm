#DP. 메모할 것: 채우는 방법의 수
def solution(n):
    answer = 0
    dp = [0] * 5001 # i번째칸 채우는 방법 수
    dp[2] = 3
    dp[4] = 11
    for i in range(6, n+1):
        # 항상 나머지 통째로 이음새 전체 연결된 2 경우 나옴
        # (i-2경우 * 2칸짜리 기본 3경우) + (i-4경우 * 이음새 2경우) + .. (2경우 * 이음새 2경우) + 전체 통채로 연결된 2경우
        if i % 2 == 0:
            dp[i] = dp[i-2] * 3 + 2 # i-2경우 + 전체 통채로 2
            for j in range(i-4, 1, -2):
                dp[i] += (dp[j] * 2) # i-4경우 + ....
            dp[i] = dp[i] % 1000000007 #여기서 나눠줘야 함!
    return dp[n]