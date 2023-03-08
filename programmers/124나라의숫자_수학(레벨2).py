def solution(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3) #인덱스이므로 n-1
        return solution(q) + '124'[r]