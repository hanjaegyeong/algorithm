#발상 중요
#부분최적해 - 그리디
#i-1값이 goal과 다르면 무조건 on
import sys
input = sys.stdin.readline

def greedy(idx):
    if ntmp[idx - 1] != goal[idx - 1]:
        ntmp[idx] = abs(ntmp[idx] - 1)
        ntmp[idx - 1] = abs(ntmp[idx - 1] - 1)
        if idx != n - 1:
            ntmp[idx + 1] = abs(ntmp[idx + 1] - 1)
        return 1
    return 0

n = int(input())
nums = list(map(int, input().rstrip()))
goal = list(map(int, input().rstrip()))
ntmp = nums[:]
cnt = 0

for i in range(1, n): # 첫번째 전구 안 켠 경우
    cnt += greedy(i)

if ntmp == goal:
    print(cnt)
    sys.exit()

cnt = 1
ntmp = nums[:]
ntmp[0] = abs(ntmp[0] - 1)
ntmp[1] = abs(ntmp[1] - 1)

for i in range(1, n): # 첫번째 전구 켠 경우
    cnt += greedy(i)

if ntmp == goal:
    print(cnt)
else:
    print(-1)
