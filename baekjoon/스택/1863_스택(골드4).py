#easy
import sys
input = sys.stdin.readline

n = int(input().rstrip())
stk = list()
ans = 0
by = 0
for i in range(n):
    x, y = map(int, input().split())
    if y > by:
        stk.append(y)
        stk.sort()
    elif y < by:
        for i in range(len(stk)-1, -1, -1):
            if stk[i] > y:
                stk.pop()
                ans += 1
        
        if y not in stk:
            stk.append(y)
            stk.sort()
    by = y

ans += len(stk)
if 0 in stk:
    ans -= 1

print(ans)