# 연속한 유일수 수열 경우의 수
# 수열길이 +1 될때마다 경우의수 1 3 6 10 ... 즉, +=1 +=2 +=3 씩 증가

n = int(input())
nums = list(map(int, input().split()))
mem = [0] * 100001
l, r = 0, 0
result = 0

while l <= r and r < n:
    if not mem[nums[r]]: #유일수: r += 1
        mem[nums[r]] = 1
        r += 1
        result += r - l
    else: #중복수: l += 1
        while mem[nums[r]]:
            mem[nums[l]] = 0
            l += 1

print(result)