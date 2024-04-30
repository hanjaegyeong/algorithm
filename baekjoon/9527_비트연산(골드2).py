# i번째 인덱스의 비트는 2^i개의 0과 1을 교대로 반복
# 0번째: 0 1 0 1..., 1번째: 0 0 1 1 0 0... 2번째: 0 0 0 0 1 1 1 1...
# 각 인덱스 i마다 n까지 합 카운팅
def count_set_bits_up_to(n):
    count = 0
    i = 0 # i==0일때가 0번째 인덱스 비트!
    while (1 << i) <= n: # 2^i가 n이하인 동안
        # 블록 크기: 2^i개의 0, 2^i개의 1
        total_pairs = 1 << (i + 1)
        # 완전히 끝낸 블록 쌍 개수
        complete_blocks = n // total_pairs
        # 완전블록 내 1 카운팅: (완전블록*2^i)개의 1
        count += complete_blocks * (1 << i)
        # 남은 부분에서 1의 개수 계산
        # 처음 0은 0일 때니까 4번째부터 1로, 1씩당겨짐-> +1필요
        count += max(0, (n % total_pairs) - (1 << i)+1)
        i += 1

    return count

def count_set_bits(a, b):
    return count_set_bits_up_to(b) - count_set_bits_up_to(a - 1)

A, B = map(int, input().split())
print(count_set_bits(A, B))