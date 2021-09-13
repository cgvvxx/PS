# Baekjoon 2224 - 명제 증명
# Silver 1
# 최단 거리 - 플로이드 워셜


def char_to_num(c):
    if c.isupper():
        return ord(c) - 65
    else:
        return ord(c) - 71
    
def num_to_char(n):
    
    if n <= 25:
        n += 65
    else:
        n += 71
    
    return chr(n)

def print_sen(i, j):
    
    return f'{num_to_char(i)} => {num_to_char(j)}'
    

n = int(input())
m = 52

graph = [[0]*m for _ in range(m)]
for _ in range(n):
    s = input()
    prv, nxt = s[0], s[-1]
    graph[char_to_num(prv)][char_to_num(nxt)] = 1
    
cnt = 0
for i in range(m):
    for j in range(m):
        for k in range(m):
            graph[j][k] = any([graph[j][k], graph[j][i]&graph[i][k]])

printed = []
for i in range(m):
    for j in range(m):
        if i == j:
            continue
            
        if graph[i][j]:
            printed.append(print_sen(i, j))
            
print(len(printed))
for i in printed:
    print(i)
    
    
# 노드의 수가 52개 이므로 Floyd-Warshall 활용
# 11403과 거의 비슷