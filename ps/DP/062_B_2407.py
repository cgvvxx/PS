# Baekjoon 2407 - 조합
# Silver 2
# DP

n, m = map(int, input().split())
combs = [[], [], [1, 2, 1]]

for i in range(3, n+1):
    i_comb = [1]
    this = combs[i-1]
    for j in range(len(this)-1):
        i_comb.append(this[j] + this[j+1])
        if i == n and j == m:
            break
    i_comb.append(1)
    combs.append(i_comb)
    
    
print(combs[n][m])