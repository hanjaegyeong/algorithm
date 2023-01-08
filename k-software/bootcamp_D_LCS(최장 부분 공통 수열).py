#dp_LCS(최장 부분 공통 수열)

t = int(input())
for _ in range(t):
    a_len, *a = list(map(int, input().split()))
    b_len, *b = list(map(int, input().split()))
    graph = [[0] * (b_len+1) for _ in range(a_len+1)]

    for i in range(1, a_len+1):
        for j in range(1, b_len+1):
            if a[i-1] == b[j-1]:
                graph[i][j] = graph[i-1][j-1] + 1
            else:
                graph[i][j] = max(graph[i-1][j], graph[i][j-1])

    print(graph[-1][-1])