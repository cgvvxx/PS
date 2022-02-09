# Baekjoon 2961 - 도영이가 만든 맛있는 음식
# Silver 1
# 완전탐색


from itertools import combinations

n = int(input())
sours = []
sweets = []
for _ in range(n):
    s, b = map(int, input().split())
    sours.append(s)
    sweets.append(b)

ans = 10**10
for i in range(1, n+1):
    for comb in combinations(range(n), i):
        sour = 1
        sweet = 0
        for idx in comb:
            sour *= sours[idx]
            sweet += sweets[idx]
        
        check = abs(sour - sweet)
        if check < ans:
            ans = check
            
print(ans)


# 단순 완전 탐색 (최대 경우의 수 2**10)