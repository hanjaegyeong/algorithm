import sys
input = sys.stdin.readline

n = int(input().rstrip())
l = list(map(int, input().rstrip().split()))
s = [[0, 1000000]] # 거리, 건물위치(번호)
result = list(list() for _ in range(n))
cnt = [0] * n

# 왼쪽에서 오른쪽으로 스캔
for i in range(n):
    while s and l[i] >= s[-1][0]:
        s.pop()
    if s:
        result[i] = s[-1][1]
        cnt[i] += len(s)
    s.append([l[i], i+1])

# 오른쪽에서 왼쪽으로 스캔
s = [[0, 1000000]] # 스택 초기화
for i in range(n-1, -1, -1):
    while s and l[i] >= s[-1][0]:
        s.pop()
    if s:
        # 거리 더 가까우면 result 갱신
        if (result[i] and abs(i+1-result[i]) > abs(i+1-s[-1][1])) or not result[i]:
            result[i] = s[-1][1]
    cnt[i] += len(s)
    s.append([l[i], i+1])

# 결과 출력
for i in range(n):
    if result[i]:
        print(cnt[i], result[i])
    else:
        print(cnt[i])
