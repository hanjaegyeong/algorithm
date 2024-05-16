#분할정복
n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

#행렬곱
def arrmul(x, y):
    r = list([0] * n for _ in range(n))
    for i in range(n):
        for j in range(n):
            for k in range(n):
               r[i][j] += x[i][k] * y[k][j] % 1000 #행기준i * 열기준j 돌리기
    return r

#분할정복
def daq(arr, sq):
    if sq == 1:
       return arr
    
    divarr = daq(arr,sq//2)
    
    if sq % 2 == 0:
        return arrmul(divarr, divarr)
    else:
        return arrmul(arrmul(divarr, divarr) , arr)
    
result = daq(a, b)

for i in range(n):
    for j in range(n):
        result[i][j] %= 1000
    print(*result[i])