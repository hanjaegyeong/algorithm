# re풀기 - 기록 로직
n, k = map(int, input().split()) #개수, 최대무게
items = list(list(map(int, input().split())) for _ in range(n)) # 무게, 가치

# dp = i 무게를 넣었을 때 최대 가치
dp = [0] * (k+1)

# 역순기록!!! 중요
# 이중 업데이트 피하기 위해: dp에서는 진행방향 값이 업데이트되게 만들면 안됨!
for w, v in items: #items[i] 넣는 경우
    for j in range(k, w-1, -1): #무게 j가 될 때 가치 메모
        if dp[j-w]+v >= dp[j]:
            dp[j] = dp[j-w]+v

print(max(dp))