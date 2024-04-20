import sys
input = sys.stdin.readline

for _ in range(3):
    n = int(input())
    coins = list()
    half = 0
    result = 0

    for _ in range(n):
        coin, x = map(int, input().rstrip().split())
        coins.append([coin, x])
        half += coin * x
    
    if half % 2: #안 나눠 떨어지면 어차피 안됨
        print(0)
        continue

    #나눠 떨어지면 반띵
    half //= 2 #dp[half] == True면 성공

    dp = [False] * (half+1) # idx원이 가능한지 메모
    dp[0] = True

    #dp
    for coin, coincnt in coins:
        #역방향 메모 - 정방향이면 True된 곳 기준으로 +C가 다 True돼서 동전개수 초과
        #half에서 j-coin가 0되는 지점까지
        for j in range(half, coin-1, -1): 
            #+coin 했을 때 True로 만들려고 j-coin인 경우 True인지 확인
            #처음엔 유일 True인 dp[0] 지점부터 if문 통과해서 True 메모 시작
            if dp[j-coin]:
                for x in range(coincnt): #모든 동전개수 경우 추가
                    if (j + coin * x) <= half: # j가 이미 +coin한 값이므로
                        dp[j + coin * x] = True
                    else:
                        break

    if dp[half]:
        result = 1

    print(result)