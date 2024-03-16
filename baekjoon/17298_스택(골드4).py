from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
stk = deque()
result = [-1] * n #각 인덱스에 메모

#수열 뒤에서부터 비교
for i in range(n-1, -1, -1):
    
    while stk and a[i] >= stk[-1]: #현재수가 더 큰 동안 pop
        stk.pop()
       
    if stk: #모든 pop 이후 스택에 남은 값 있으면 가장 왼쪽값 선택
        result[i] = stk[-1]
    
    stk.append(a[i]) #현재값 스택에 넣기
    
print(*result)