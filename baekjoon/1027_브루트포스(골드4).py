#easy
n = int(input())
heights = list(map(int, input().split()))
result = 0

for i in range(n):
    cnt_left = 0
    cnt_right = 0

    # 왼쪽 빌딩들 검사
    max_slope = float('-inf')
    for j in range(i - 1, -1, -1):
        slope = (heights[i] - heights[j]) / (i - j)
        if slope > max_slope:
            max_slope = slope
            cnt_left += 1

    # 오른쪽 빌딩들 검사
    max_slope = float('-inf')
    for j in range(i + 1, n):
        slope = (heights[j] - heights[i]) / (i - j)
        if slope > max_slope:
            max_slope = slope
            cnt_right += 1

    result = max(result, cnt_left + cnt_right)

print(result)
