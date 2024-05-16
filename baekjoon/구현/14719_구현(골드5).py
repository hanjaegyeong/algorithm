#14719번. 구현
#i칸의 rain = 양 옆의 max높이 중 min높이 - i칸높이

h, w = map(int, input().split()) #가로, 세로
field = list(map(int, input().split()))
rain = 0

for i in range(1, len(field)-1):
    leftmax = max(field[:i])
    rightmax = max(field[i+1:])
    minh = min(leftmax, rightmax)
    if minh > field[i]:
        rain += minh - field[i]
print(rain)