import sys
input = sys.stdin.readline

# mid, r, l은 거리값
def bs(tar):
    l, r = 1, home[-1]-home[0] #최소거리차, 최대거리차
    result = 0
    while (l <= r):
        mid = (l+r) // 2
        cnt = 1 #home[0]에 설치하고 시작
        pre = home[0]
        for i in range(1, n):
            if home[i] - pre >= mid: # 거리차가 mid보다 큰 애들만 카운팅
                cnt += 1
                pre = home[i]
        if cnt >= tar:
            l = mid + 1
            result = mid
        else:
            r = mid - 1
    return result

n, c = map(int, input().split())
home = [0] * n
for i in range(n):
    home[i] = int(input())

home.sort()
print(bs(c))