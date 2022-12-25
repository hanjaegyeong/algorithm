#22251 구현_pypy3로 제출
#자릿수 한꺼번에 비교 알고리즘 타 코드 참조

num_list = [
    [1,1,1,1,1,1,0],[0,0,1,1,0,0,0],[0,1,1,0,1,1,1],[0,1,1,1,1,0,1],
    [1,0,1,1,0,0,1],[1,1,0,1,1,0,1],[1,1,0,1,1,1,1],[0,1,1,1,0,0,0],
    [1,1,1,1,1,1,1],[1,1,1,1,1,0,1]
    ]

def count_num():
    ans = 0
    for i in range(1, n+1): #1층부터 n층까지
        if i == x:
            continue
        cnt = 0
        now_floor, want_floor = x, i #현재층, i층 비교
        #now층과 want층 모든 자릿수 한꺼번에 비교
        for j in range(k):
            for z in range(7):
                #마지막 자릿수 비교***
                if num_list[now_floor%10][z] != num_list[want_floor%10][z]:
                    cnt += 1
            #마지막 자릿수 없애기***
            now_floor //= 10
            want_floor //= 10
        #현재층, i층 비교해서 p번 반전 이하면 ans+=1
        if cnt <= p:
            ans += 1
    return ans

n, k, p, x = map(int, input().split()) #n층까지, k자리, p번 반전, x층
print(count_num())