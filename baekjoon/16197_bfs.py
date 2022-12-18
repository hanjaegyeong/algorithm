#칸없으면 떨어짐, 동전있어도 이동가능, 벽이면 유지
#두 동전 중 하나만 보드에서 떨어뜨리기 위한 최소cnt: bfs
#둘다떨어지거나, 불가, 10번초과면 return -1
import sys
from collections import deque
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while q:
        ox, oy, tx, ty, cnt = q.popleft()
        if cnt > 10:
            return -1
        for i in range(4):
            onx, ony = ox + dx[i], oy + dy[i]
            tnx, tny = tx + dx[i], ty + dy[i]
            #둘 다 내부일 때
            if 0 <= onx < n and 0 <= ony < m and 0 <= tnx < n and 0 <= tny < m:
                if field[onx][ony] == "#":
                    onx, ony = ox, oy
                if field[tnx][tny] == "#":
                    tnx, tny = tx, ty
                q.append((onx, ony, tnx, tny, cnt+1))
            #둘 다 떨어질 때
            elif (not 0 <= onx < n or not 0 <= ony < m) and (not 0 <= tnx < n or not 0 <= tny < m):
                continue
            #하나 떨어질 때
            else:
                return cnt           
    #둘 다 안 떨어질 때
    return -1

n, m = map(int, input().split())
field = []
istwo = False
for i in range(n):
    field.append(input())
for i in range(n):
    for j in range(m):
        if field[i][j] == 'o':
            if not istwo:
                ox, oy = i, j
                istwo = True
            else:
                tx, ty = i, j
                break
q = deque([(ox, oy, tx, ty, 1)])
print(bfs())