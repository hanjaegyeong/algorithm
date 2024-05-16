import sys
sys.setrecursionlimit = 10 ** 8

s = input()
t = input()

# 마지막 글자 if A: 없앰
# 처음 글자 if B: 없애고 뒤집기

def bt(t):
    if t == s:
        print(1)
        sys.exit()
   
    if len(t) == 0:
        return
   
    if t[-1] == "A":
        bt(t[:-1])
   
    if t[0] == "B":
        bt(t[1:][::-1])

bt(t)
print(0)