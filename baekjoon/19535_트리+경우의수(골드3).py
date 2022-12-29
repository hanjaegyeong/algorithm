# 19535_트리+경우의수(골드3)
import sys
input = sys.stdin.readline

n = int(input())
degree = [0] * (n+1) #각 노드 간선 수
tree = []
dcnt, jcnt = 0, 0
for i in range(n-1):
    u, v = map(int, input().split())
    tree.append([u, v])
    degree[u] += 1
    degree[v] += 1

# ㄷ: 2,3번째(연결노드) 각각 잡고 (연결노드-1)*(연결노드-1) 경우의수
# -1이유: 서로 연결된 경우는 이미 상정되었으므로
for u, v in tree:
    dcnt += (degree[u] - 1) * (degree[v] - 1)

# ㅈ: 2번째 노드 잡고 nC3 경우의수
for i in range(1, n+1):
    if degree[i] >= 3:
        jcnt += (degree[i] * (degree[i]-1) * (degree[i]-2)) / 6 #nC3***

if dcnt > 3 * jcnt:
    print("D")
elif dcnt < 3 * jcnt:
    print("G")
else:
    print("DUDUDUNGA")