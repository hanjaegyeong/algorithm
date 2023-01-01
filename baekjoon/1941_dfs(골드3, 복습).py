#1941_dfs(골드3, 복습)
#경로 한줄 아니라 중간에 튀어나오는 부분 처리***
#타 코드 참고함
import sys
sys.setrecursionlimit(10**8)
dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(arr, cnt, s, y): #경로리스트, 현재 인원, 다솜파 수, 도연파 수
    if y > 3: #임도연파 4명 넘어버리면
        return
    if cnt == 7: #7명 되면
        arr.sort() #모든 지점 정렬해서
        result_set.add(tuple(arr)) #순서 다른 arr 중복 경우들 다 제거***
        return
    
    #현재 경로까지 모든 지점의 인접점 조사***
    adjacents = [] #인접 리스트
    for node in range(len(arr)): #포함된 모든 지점에서 인접점 추가
        for i in range(4):
            nx = arr[node][0] + dxdy[i][0]
            ny = arr[node][1] + dxdy[i][1]
            if 0 <= nx < 5 and 0 <= ny < 5 and not (nx, ny) in arr:
                adjacents.append((nx, ny))
    for nx, ny in adjacents: #각 인접점 방문 경우
        if graph[nx][ny] == 'S': #이다솜파면
            dfs(arr+[(nx,ny)], cnt+1, s+1, y)
        else:                   #임도연파면
            dfs(arr+[(nx,ny)], cnt+1, s, y+1)

graph = [input() for _ in range(5)]
result_set = set()

for i in range(5):
    for j in range(5):
        if graph[i][j] == 'S': #이다솜파 있는 곳에서만 시작
            dfs([(i, j)], 1, 1, 0)

print(len(result_set))