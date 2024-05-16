# 총 n획 만드는 최대,최소수
from collections import deque
import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input().rstrip())

    #minl[i]만드는 데 i개 사용
    minl = [0, 0, 1, 7, 4, 2, 6, 8, 10, 18, 22, 20] # 2~11
    minans, maxans = deque(), deque()
    minn, maxn = n, n

    #최대수
    #1(2개) 쓰는 게 이득
    while True:
        if maxn == 0:
            break
        elif maxn == 3:
            maxans.appendleft(7)
            break
        else: #짝수는 무조건 2개 추가
            maxans.appendleft(1)
            maxn -= 2
   
    #최소수
    #8(7개) 쓰는 게 이득
    while True:
        if minn == 0:
            break
        elif minn == 17:
          minans.appendleft(200)
          break
        elif minn > 11:
            minans.appendleft(8)
            minn -= 7
        else:
            minans.appendleft(minl[minn])
            break

    print(''.join(map(str, minans)), end=' ')
    print(''.join(map(str, maxans)))