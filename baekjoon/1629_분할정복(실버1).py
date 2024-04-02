#분할정복
import sys
input = sys.stdin.readline

# a**b %c
# 제곱 반띵 후 ** 2 해주면 시간 단축
# ex) 3**16 = (3**8)**2
def dac(a, b, c): # a**b %c
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (dac(a, b//2, c) ** 2 % c)
    else:
        return ((dac(a, b//2, c) ** 2) * a % c)

a, b, c = map(int, input().split())
print(dac(a, b, c))