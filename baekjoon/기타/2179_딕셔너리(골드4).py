# 딕셔너리 카운팅
import sys
input = sys.stdin.readline

n = int(input())
arr = list(input().rstrip() for _ in range(n))
dic = dict() #prefix:cnt 딕셔너리
result = list()
isovertwo = 0

for i in range(n):
    for j in range(len(arr[i])):
        prefix = arr[i][:j+1]
        if prefix not in dic:
            dic[prefix] = 1
        else:
            dic[prefix] += 1
            isovertwo = 1
    
# key(접두사)길이 기준 내림차순, 같은 경우엔 value(cnt) 기준 내림차순
dlist = sorted(dic.items(), key=lambda x: (-len(x[0]), -x[1]))

preans = dlist[0][0]
if dlist[0][1] == 1:
    for i in range(len(dlist)):
        if dlist[i][1] > 1:
            preans = dlist[i][0]
            break

for i in range(n):
    for j in range(len(arr[i])):
        prefix = arr[i][:j+1]
        if prefix == preans:
            result.append(arr[i])
    if len(result) == 2:
        break

for i in result:
    print(i)