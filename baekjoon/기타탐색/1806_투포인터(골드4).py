#부분합 s 이상 중 가장 짧은 연속수열
n, s = map(int, input().split())
nums = list(map(int, input().split()))
result = float('inf')
l, r = 0, 0 #둘 다 0부터 시작!!
nsum = nums[0]

# l <= r 조건 달면 뒤에서 최소길이 나올 경우 측정불가
# 조건 없이도 l <= r되면 nsum < s이므로 자동 r증가
while True: 
    if nsum < s:
        if r+1 < n:
            r += 1
            nsum += nums[r]
        else:
            break
    else:
        result = min(r - l + 1, result)
        nsum -= nums[l]
        l += 1

if result != float('inf'):
    print(result)
else:
    print(0)