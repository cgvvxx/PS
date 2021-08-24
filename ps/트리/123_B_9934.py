# Baekjoon 1991 - 트리 순회
# Silver 1
# 그래프 - 트리


k = int(input())
inordered = list(map(int, input().split()))

trees = [[] for _ in range(k)]
m = 0
while m < k:
    idx = 2**(k-1-m)
    for i in range(2**m):
        trees[m].append(inordered[idx + (i*2**(k-m)) - 1])
    m += 1
    
for l in trees:
    print(*l)


# 완전 이진 트리이므로 2의 거듭제곱 꼴로 index가 주어짐
# 이를 while과 for문 반복해서 index 지정