#힙 이해! 중요
#항상 가장 작은애들로만 합치기
#자동 정렬되는 힙 이용
import heapq

t = int(input())
for _ in range(t):
    n = int(input())
    files = list(map(int, input().split()))
    heapq.heapify(files) #힙으로 만들어서 사용!
    cost = 0

    while len(files) > 1:
        new = heapq.heappop(files) + heapq.heappop(files)
        heapq.heappush(files, new)
        cost += new
        
    print(cost)