# 스택 (발상찾기)
n = int(input())
towers = list(map(int, input().split()))
stk = list() #타워인덱스
ans = [0] * n

# 전이 더 클 경우 ans[i] = 전인덱스+1
# 내가 더 클 경우 stk.pop()
# 두 경우 다 스택에 넣기
for i in range(n):
    while stk:
        if towers[i] < towers[stk[-1]]:
            ans[i] = stk[-1] + 1
            break
        else:
            stk.pop()    
    stk.append(i)

print(*ans)