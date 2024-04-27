n, a, b = map(int, input().split())
answer = []

for i in range(1, a): #최대수는 빼고 1부터
    answer.append(i)

# 최대수는 하나만 솟아 있어야 함
answer.append(max(a, b))

for i in range(b-1, 0, -1): #최대수는 빼고 1까지(사전순)
    answer.append(i)

if a + b -1 > n:
    print(-1)
else: # 앞에 남은 공간은 다 1로 채우고 맨 뒤에 answer
    cnt = 0
    print(answer[0], end=' ') # a가 1인 경우를 위해
    while cnt < (n - len(answer)):
        print(1, end=' ')
        cnt += 1
    print(*answer[1:])