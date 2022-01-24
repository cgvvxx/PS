# Baekjoon 16439 - 치킨치킨치킨
# Silver 4
# 완전탐색


from itertools import combinations

def get_score(c):
    
    score = 0
    for p in preferences:
        score += max(p[i] for i in c)
    
    return score


n, m = map(int, input().split())
preferences = []
for _ in range(n):
    preferences.append(list(map(int, input().split())))
    
score = 0
for comb in combinations(range(m), 3):
    score = max(score, get_score(comb))

print(score)


# 경우의 수가 크지 않은 완전탐색
# m이 최대 30이므로 30C3이 최대 경우의 수라 그냥 모든 경우에 대해서 선호도의 합의 최댓값 계산