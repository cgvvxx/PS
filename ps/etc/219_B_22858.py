# Baekjoon 22858 - 원상 복구 (small)
# Silver 3


def shuffle(pi: list, di: list):
    
    ni = [0] * n
    for idx, num in enumerate(di):
        ni[num-1] = pi[idx]
        
    return ni


def shuffle_k(pi: list, di: list, k: int):
    
    for _ in range(k):
        pi = shuffle(pi, di)
        
    return pi


n, k = map(int, input().split())
si = list(map(int, input().split()))
di = list(map(int, input().split()))

print(*shuffle_k(si, di, k))


# 거꾸로 연산을 하려면 di의 idx에 있는 숫자의 번호가 새로운 리스트의 idx
# 시간복잡도 ~ O(NK)인데 통과해서 최적화 X
# 시간을 줄이려면
# 1. 주어진 di에 대해 최소 주기(p)를 구한 후
# 2. k % p 번 shuffle하면 될듯?
# 이 경우 제출했는데 통과해서 패스..