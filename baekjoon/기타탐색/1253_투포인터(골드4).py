#easy
#음수도 가능
#l, r == i인 경우는 불가
n = int(input())
nums = sorted(list(map(int, input().split())))
ans = 0
for i in range(n): # 같은 수 가능하므로 0부터
    l, r = 0, n-1
    while l < r:
        s = nums[l] + nums[r]
        if i == l:
            l += 1
        elif i == r:
            r -= 1
        elif s == nums[i] and i != l and i != r:
            ans += 1
            break
        elif s < nums[i]:
            l += 1
        else:
            r -= 1

print(ans)