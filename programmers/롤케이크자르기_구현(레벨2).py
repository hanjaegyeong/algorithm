# 종류와 개수: set, Counter 이용
# 동생이 다 가진채로 시작
# 왼쪽부터 철수꺼 하나씩 증가
from collections import Counter
def solution(topping):
    cnt = 0
    # 철수, 동생 종류
    A, B = set(), Counter(topping)
    # 철수, 동생 개수
    a, b = 0, len(B)
    for i in topping:
        B[i] -= 1
        if B[i] == 0:
            b -= 1
        if not i in A:
            A.add(i)
            a += 1
        if a == b:
            cnt += 1
    return cnt