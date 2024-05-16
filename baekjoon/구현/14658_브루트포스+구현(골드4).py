# l*l을 옮겨 최대한 많은 stars 튕겨내고 남은 stars 개수
# n,m기준 for문->시간초과. s기준 for문으로 해야 함
import sys
input = sys.stdin.readline

n, m, l, s = map(int, input().rstrip().split()) #가로,세로,트램펄린길이,별똥별수
stars = list(list(map(int, input().rstrip().split())) for _ in range(s))
result = 0

# 두 점 잡고 각 수직, 수평선의 교차점을 좌하단 꼭짓점으로 하는 사각형
# 해당 범위 내에 들어오는지 판단
for i in range(s): #수평기준점 i+l
    for j in range(s): #수직기준점 j+l
        maxstar = 0
        for k in range(s): #k번째 star가 해당 범위내에 있는지
            if stars[i][0] <= stars[k][0] <= stars[i][0]+l and stars[j][1] <= stars[k][1] <= stars[j][1]+l:
                maxstar += 1
        result = max(result, maxstar)

print(s - result)