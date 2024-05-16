# 투포인터
n = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())
result = 0
l, r = 0, n-1

while (l < r):
    s = nums[l] + nums[r]
    if (s == x):
        result += 1
        l += 1
    elif (s > x):
        r -= 1
    else:
        l += 1

print(result)