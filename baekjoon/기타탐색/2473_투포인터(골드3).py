# 투포인터
n = int(input())
rqs = sorted(list(map(int, input().split())))
rsum = 4000000000
flag = 0
result = []

for i in range(n-2): #i값이므로!!
    l, r = i+1, n-1
    while (l < r):
        s = rqs[i] + rqs[l] + rqs[r]  
        if abs(s) < rsum:
            result = [rqs[i], rqs[l], rqs[r]]
            rsum = abs(s) 

        if s == 0:
            
            break
        elif s > 0:
            r -= 1
        else:
            l += 1
       

print(*result)