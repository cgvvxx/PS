# Baekjoon 14889 - 스타트와 링크
# Silver 3
# 완전탐색

from itertools import combinations

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))
    
def split_comb(n):
    
    splited = []
    for comb1 in combinations(range(n), n//2):
        comb2 = []
        for j in range(n):
            if j not in comb1:
                comb2.append(j)
        splited.append([list(comb1), comb2])
    
    return splited[:len(splited)//2]

scores = []
splited = split_comb(n)
for this in splited:
    score = 0
    for idx, i in enumerate(this):
        for j in combinations(i, 2):
            if idx == 0:
                score += arr[j[0]][j[1]]
                score += arr[j[1]][j[0]]
            else:
                score -= arr[j[0]][j[1]]
                score -= arr[j[1]][j[0]]
    scores.append(abs(score))

print(min(scores))