# 연속된 소수의 합 경우의 수
# 투 포인터
# 에라토스테네스의 체 : 제곱근 기준으로 약수 대칭 이용
import math

def get_pn(n):
    pns = [i for i in range(n+1)]
    
    for i in range(2, int(math.sqrt(n))+1): # 제곱근까지만 계산
        if pns[i] == 0: #이미 제외된 애들은 패스
            continue

        for j in range(i*i, n+1, i): #본인 제곱근 남기고 배수들 제외 
            pns[j] = 0
    return [i for i in pns[2:] if pns[i]]

def tp(n):
    l, r = 0, 1
    result = 0

    while (r <= len(pn) and l <= r):
        s = sum(pn[l:r])
        if s == n:
            result += 1
            r += 1
        elif s > n:
            l += 1
        else:
            r += 1
    return result

n = int(input())
pn = get_pn(n)
print(tp(n))