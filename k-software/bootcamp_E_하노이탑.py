#하노이의 탑
#출력: 원반 n개, a번째 원반이 b번에서 c번으로 이동

def hanoi_tower(num, a, c, b):
	if num == 1:
		print(num, a, c)
		return
	hanoi_tower(num-1, a, b, c)
	print(num, a, c)
	hanoi_tower(num-1, b, c, a)

n = int(input())
for i in range(1, n+1):
	print(i)
	hanoi_tower(i, 1, 3, 2)