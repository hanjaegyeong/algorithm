# 19538_bfs(골드4)
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while q:
        x = q.popleft()
        for i in user[x]: #x와 연결된 사람 i
            if not visited[i]:
                rumercnt[i] += 1 #관계도 등장 + 1
                if rumercnt[i] >= len(user[i])/2: #과반 전염시
                    visited[i] = 1
                    answer[i] = answer[x] + 1
                    q.append(i)

n = int(input())
visited = [0]*(n+1)
user = [0] #관계도
for i in range(n):
    *a, b = map(int, input().split())
    user.append(a)

rumercnt = [0] * (n+1) #관계도 등장 횟수
answer = [-1] * (n+1)

m = int(input()) #루머유포자 수
rumers = list(map(int, input().split())) #루머유포자
q = deque()
for i in rumers:
    visited[i] = 1
    answer[i] = 0
    q.append(i)
bfs()
print(*answer[1:])