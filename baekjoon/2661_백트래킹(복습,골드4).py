#2661_백트래킹(복습,골드4)
#인접 중복수열x 가장작은수열
#중복체크: 문자열 1개씩, 2개씩 ,3 개씩 ... 길이//2 까지 체크

def back_tracking(idx): #idx: 현재 체크할 자릿수

    for i in range(1, (idx//2) + 1): #반띵 중복체크
        if s[-i:] == s[-2*i:-i]: #양방향 same: 탈락
            return -1

    if idx == n: #마지막 자리면
        for i in range(n):
            print(s[i], end = '') #수열 출력하고 끝
        return 0

    for i in range(1, 4): #다음 들어갈 수 고르기
        s.append(i) #넣고
        if back_tracking(idx + 1) == 0: #재귀->return 0(마지막자리까지 간 경우)
            return 0 #탈출
        s.pop() #마지막까지 못가고 중복체크 걸리면 pop하고 다시

n = int(input())
s = []
back_tracking(0)