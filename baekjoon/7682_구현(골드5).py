#easy
import sys
input = sys.stdin.readline

def iswin(sign):
    for i in range(0, 7, 3): #가로
        if t[i] == t[i+1] == t[i+2] == sign:
            return 1
    for i in range(3): #세로
        if t[i] == t[i+3] == t[i+6] == sign:
            return 1
    if t[0] == t[4] == t[8] == sign:
        return 1
    if t[2] == t[4] == t[6] == sign:
        return 1
    return 0

while True:
    t = list(input().rstrip())
    if t == list('end'):
        break
    ocnt = 0
    xcnt = 0
    dcnt = 0
    for i in t:
        if i == 'O':
            ocnt += 1
        elif i == 'X':
            xcnt += 1
        else:
            dcnt += 1
    if iswin('X') and iswin('O'):
        print("invalid")
    elif dcnt == 0 and ocnt == xcnt - 1: #꽉 찬 경우
        if iswin('O'):
            print("invalid")
        else:
            print("valid")
            continue
    elif dcnt != 0 and ocnt == xcnt: # O 승리 시
        if iswin('O'):
            print("valid")
        else:
            print("invalid")
    elif dcnt != 0 and xcnt == ocnt + 1: # X 승리 시
        if iswin('X'):
            print("valid")
        else:
            print("invalid")
    else:
        print("invalid")