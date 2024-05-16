# x행의 y이상, y열의 x이상 삭제
# 중력의 영향 -> 윗칸 <= 아랫칸
import sys
input = sys.stdin.readline
  
n, q = map(int, input().rstrip().split()) #행 개수, 레이저수
# i층에 nemos[i]마리 네모
nemos = list(map(int, input().rstrip().split()))
m = max(nemos)

for i in range(q):
    ans = 0
    y, x = map(int, input().split())
    x, y = x-1, y-1
    
    if x > n-1 or y > m:
        print(0)
        continue

    # y 이상인 열에서 행의 최댓값
    l, r = 0, len(nemos)-1 # l, r, mid: 특정 행
    result = 0
    while l <= r:
        mid = (l+r) // 2
        if nemos[mid] >= y+1: #nemos[i]: 각 행의 열 길이
            result = mid
            l = mid + 1
        else:
            r = mid - 1

    ver = nemos[x] - y + 1 #열값 계산 - x행의 y이상 개수
    hor = r - x # 행값 계산 - y열의 x이상 개수
    ans += ver + hor - 1

    if ans < 0:
        print(0)
    else:
        print(ans)