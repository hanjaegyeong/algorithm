# if len(plugs) == n and x[i] not in plugs:
# x[i+1:].index(x[i]) 값이 제일 큰 애부터 remove

n, k = map(int, input().split())
x = list(map(int, input().split()))
plugs = list()
cnt = 0

for i in range(k):
    if x[i] not in plugs:
        if len(plugs) == n and i < k-1: #플러그 뽑기
            maxi, popx = -1, 0 #가장먼인덱스, 뽑을애
            for j in plugs:
                if j in x[i+1:]:
                    popi = x[i+1:].index(j)
                    if popi > maxi:
                        maxi = popi
                        popx = j
                else: # 재등장 x시 바로 채택
                    maxi = 1
                    popx = j
                    break
            if maxi != -1: #재등장 시점이 제일 나중
                plugs.remove(popx)
            cnt += 1
        elif len(plugs) == n and i == k-1: #마지막 자리
            plugs.pop() #아무거나 뽑기
            cnt += 1
        # 플러그 꽂기
        plugs.append(x[i])

print(cnt)