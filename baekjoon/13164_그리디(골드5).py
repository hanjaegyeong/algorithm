# [양값 차, 인덱스(끝값)] 리스트에 저장 후 역정렬 후 k-1개만큼 잘라서 비용 계산

n, k = map(int, input().split()) #학생수, 조 개수
heights = list(map(int, input().split()))
diff = list()
cut = list() #끊을 곳 인덱스
result, isfirst = 0, 1
l = 0

for i in range(n-1):
    diff.append([heights[i+1] - heights[i], i])
diff.sort(reverse=True)

for i in range(n-1):
    if k == 1:
        break
    cut.append(diff[i][1])
    k -= 1
cut.sort(reverse=True)

for i in range(n):
    if not cut:
        result += heights[-1] - heights[i]
        break
    elif isfirst:
        l = heights[i]
        isfirst = 0
    if cut and i == cut[-1]:
        result += heights[i] - l
        cut.pop()
        isfirst = 1
        
print(result)