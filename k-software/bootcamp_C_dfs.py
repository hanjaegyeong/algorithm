# dfs
# 현재 남은 타일 중에서 최근에 쌓인 타일 위에 올라갈 수 있는 타일을 고르고 재귀
# 남은 타일 1차원 리스트에 담기
# 최대길이 cnt 갱신
# for문으로 모든 타일 포함 경우 돌림

import sys
import copy
sys.setrecursionlimit(10**8)

# 현재보다 크거나 같으면 넣기
def dfs(now, cnt, least_tile): #현재타일(가로,세로), cnt, 남은타일들
    global ans
    tmptiles = copy.deepcopy(least_tile)
    ans = max(ans, cnt)
    for i in range(len(least_tile)):
        if least_tile[i][0] >= now[0] and least_tile[i][1] >= now[1]:
            tmptiles.pop(i)
            dfs(least_tile[i], cnt+1, tmptiles) #넣은 경우
            tmptiles = copy.deepcopy(least_tile) #안넣은 경우

t = int(input())
for _ in range(t):
    n = int(input())
    tile = []
    ans = 0
    for _ in range(n):
        a, b = map(int, input().split())
        if a > b:
            tile.append([a, b])
        else:
            tile.append([b, a])
    for i in range(n):
        tmptile = copy.deepcopy(tile)
        paratile = tmptile.pop(i)
        dfs(paratile, 1, tmptile) #여기 for로 고치기
    print(ans)