#dfs, 모든경우 끝까지 탐색
#일치하는 집합 최대길이
#시작점으로 돌아오는 체인 완성 안되면 배제. (중간에 중복 숫자 나올 경우)

import sys
input = sys.stdin.readline

def dfs(sp, lp): 
    if field[lp] == field[sp]: #start면 체인완성. 세트내용 all추가
        numset.add(field[lp])
        resultset.update(numset)
        return
    elif field[lp] in numset: #elif in set: 체인불가 s배제
        return
    else:
        numset.add(field[lp])
        dfs(sp, field[lp])

n = int(input())
field = [0]
resultset = set()
for _ in range(n):
    field.append(int(input()))
for i in range(n):
    numset = set()
    if i+1 not in resultset:
        dfs(i+1, field[i+1])
resultlist = list(resultset)
resultlist.sort()
print(len(resultlist))
for i in resultlist:
    print(i)