#구멍 지날 때마다 크기-=1
#도토리<=구멍: 떨어짐
#떨어지는 구멍 번호 순서대로 출력
from bisect import bisect_left
n = int(input())
holes = list(map(int, input().split())) #i번째 구멍크기
q = int(input())
dotos = list(map(int, input().split())) #i번째 도토리크기
result = list()

msize = [0] * n
msize[0] = holes[0]
for i in range(1, n):
    if holes[i] + i < msize[i-1]:
        msize[i] = msize[i-1] #사이즈가 이전보다 작으면 이전값 덮어쓰기
    else:
        msize[i] = holes[i] + i

for i in range(q):
    result.append(bisect_left(msize, dotos[i]) + 1)

print(*result)