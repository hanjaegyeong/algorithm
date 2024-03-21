def recur(level, cnt): #깊이, 정답 개수
    if level == 10:
        result[0] += 1
        return
    for i in range(1, 6):
        if level < 2 or numbers[level-1] != numbers[level-2] or numbers[level-1] != i:
            if i == ans[level]: #정답
                numbers[level] = i
                recur(level + 1, cnt + 1)
            else: #오답
                if cnt + (9 - level) < 5: #5점이상 불가
                    continue
                numbers[level] = i
                recur(level+1, cnt)

ans = list(map(int, input().split()))
result = [0]
numbers = [0] * 10
recur(0, 0)
print(result[0])