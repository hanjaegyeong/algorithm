from collections import deque

def solution(x, y, n):
    answer = 0
    visited = [0] * 1000001
    q = deque()
    q.append([x, 0]) #현재 수, 카운트
    while q:
        num, cnt = q.popleft()
        if num == y:
            return cnt
        for nxt in (num+n, num*2, num*3):
            if nxt <= y and not visited[nxt]:
                visited[nxt] = 1
                q.append([nxt, cnt+1])
    return -1