#0,0에서 n-1,n-1까지 이동. 잃는 최소비용
#dfs + dp 이용. dp리스트에 최소 ans기록

import sys
from collections import deque
input = sys.stdin.readline

nxny = [(-1,0),(1,0),(0,-1),(0,1)]
cnt = 0

def bfs():
    q = deque([[0,0]])
    while q:
        x, y = q.popleft()
        for i in nxny:
            nx, ny = x + i[0], y + i[1]
            if 0 <= nx < n and 0 <= ny < n and dp[nx][ny] > dp[x][y] + field[nx][ny]:
                q.append([nx, ny])
                dp[nx][ny] = dp[x][y] + field[nx][ny]

while True:
    cnt += 1
    n = int(input()) #0이면 게임종료
    if n == 0:
        break
    field = []
    dp = list([1000] * n for _ in range(n)) #dp에 누적 cost기록
    for _ in range(n):
        field.append(list(map(int, input().split())))
    dp[0][0] = field[0][0]
    bfs()
    print("Problem {}: {}".format(cnt, dp[n-1][n-1])) #포매팅 자꾸 까먹지 말기!