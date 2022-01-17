# Baekjoon 2578 - 빙고
# Silver 5


from collections import defaultdict

bingo_dict = dict()
for i in range(1, 6):
    j = 1
    for num in map(int, input().split()):
        bingo_dict[num] = (i, j)
        j += 1
        
cnt, ans = 0, 0
flag = True
bingo_line = defaultdict(int)
for _ in range(5):
    for num in map(int, input().split()):
        cnt += 1
        i, j = bingo_dict[num]
        bingo_line['r'+str(i)] += 1
        bingo_line['c'+str(j)] += 1
        
        if i == j:
            bingo_line['d1'] += 1
        if i + j == 6:
            bingo_line['d2'] += 1
        
        if flag and list(bingo_line.values()).count(5) >= 3:
            ans = cnt
            flag = False
            
print(ans)
    

# 어렵지 않은 구현
# 빙고판 생성 > 순서대로 숫자를 받으면서 3줄 이상 빙고일 때의 cnt
# dictionary 이용하여 빙고 여부 체크