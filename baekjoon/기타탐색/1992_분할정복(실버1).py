#중요
import sys
input = sys.stdin.readline

def daq(y, x, n):
    flag = 0
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != arr[x][y]:  # 다른 값이 하나라도 있다면
                flag = 1
                break
        if flag == 1:
            break
    
    if flag == 1:  # 모든 값이 동일하지 않은 경우
        n = n // 2  # 영역을 4등분
        print('(', end='')
        daq(y, x, n)  # 왼쪽 위
        daq(y+n, x, n)  # 오른쪽 위
        daq(y, x+n, n)  # 왼쪽 아래
        daq(y+n, x+n, n)  # 오른쪽 아래
        print(')', end='')
    else:  # 모든 값이 동일한 경우
        if arr[x][y] == '1':
            print(1, end='')
        elif arr[x][y] == '0':
            print(0, end='')

n = int(input())  # 행렬의 크기
arr = [input().rstrip() for _ in range(n)]  # 행렬 입력 받기

daq(0, 0, n)  # 분할정복 함수 호출
