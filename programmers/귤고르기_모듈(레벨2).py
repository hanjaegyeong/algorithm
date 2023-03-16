# 최빈값 k개 골랐을때 몇종류인지 리턴
# 최빈값 순서대로 뭉탱이로 넣어서 k 넘으면 cnt리턴
from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    cnt = 0
    #most_common : (최빈값, 등장횟수) 튜플
    for i in counter.most_common(k): #최빈값 6개 튜플 리스트
        k -= i[1]
        cnt += 1
        if k <= 0:
            break
    return cnt