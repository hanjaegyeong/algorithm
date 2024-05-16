# 두개 더해 0에 가깝도록
# 투포인터
n = int(input())
rq = sorted(list(map(int, input().split())))
l, r = 0, n-1
minabs = 2000000000

while (l < r):
    s = rq[l] + rq[r]
    
    if abs(s) < abs(minabs):
        minabs = abs(s)
        result = list([rq[l], rq[r]])

    if s == 0:
        result = list([rq[l], rq[r]])
        break
    elif s < 0:
        l += 1
    else:
        r -= 1

print(*result)