#bfs
#다 이어져있는지
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while q:
        now = q.popleft()
        cities = link[now]
        for i in range(len(cities)):
            if cities[i] == 1 and not visited[i]:
                q.append(i)
                visited[i] = 1

n = int(input()) #총 도시 수
m = int(input()) #여행계획 도시 수
link = list() #i번째 도시의 각 도시 연결 여부 link[i]
visited = [0] * n
q = deque() #방문 도시 번호
result = "YES"

for i in range(n):
    link.append(list(map(int, input().rstrip().split())))

plan = list(map(int, input().rstrip().split()))

q.append(plan[0] - 1)
visited[plan[0] - 1] = 1

bfs()
for i in plan:
    if visited[i-1] == 0:
        result = "NO"
print(result)