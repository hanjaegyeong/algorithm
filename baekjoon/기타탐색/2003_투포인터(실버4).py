# 투포인터
# i ~ j 합 == m 경우의 수
n, m = map(int, input().split())
a = list(map(int, input().split()))
result = 0
l, r = 0, 1

while r <= n and l <= r: #r <= n 주의!! (인덱스화하면 r-1까지로 들어가므로)
    s = sum(a[l:r])
    if s == m:
        result += 1
        r += 1
    elif s < m:
        r += 1
    else:
        l += 1

print(result)