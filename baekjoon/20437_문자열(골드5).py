# 덱으로 시간복잡도 완화
import sys
from collections import deque
input = sys.stdin.readline

abc = list("abcdefghijklmnopqrstuvwxyz")

t = int(input())

for _ in range(t):
    s = input().rstrip()
    k = int(input().rstrip())

    alp = [0] * 26 #알파벳 카운팅
    alpidxs = list(deque() for i in range(26)) #각 알파벳 등장 인덱스
    minn, maxn = 10000, 0

    for i in range(len(s)):
        idx = abc.index(s[i]) #알파벳 인덱스
        alp[idx] += 1
        alpidxs[idx].append(i)

        if alp[idx] == k:
            fstidx = alpidxs[idx][0]
            nlen = i - fstidx + 1
            minn = min(minn, nlen)
            maxn = max(maxn, nlen)

            #뒤에서 더 작은 / 큰 수열 나오는 경우 위해
            alpidxs[idx].popleft() #첫번째 등장 제거
            alp[idx] -= 1 #카운팅 -1
            
    if minn != 10001 and maxn != 0:
        print(minn, maxn)
    else:
        print(-1)