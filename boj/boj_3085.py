# solved: [3085] 사탕 게임
# https://www.acmicpc.net/problem/3085
# bruteforcing
# 
# Silver 3
# n이 최대 50이므로, 인접한 서로 다른 두개를 선택하는 경우의 수는 50C2, 약 2500 가지의 경우의 수
# 완전 탐색을 통해 각각의 경우에 대하여 행, 열의 연속되어 있는 사탕의 최대 개수 구하기

def cal_max_candy(graphs):
    
    ans = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if graphs[i][j] == graphs[i][j-1]:
                cnt += 1
                if cnt > ans:
                    ans = cnt
            else:
                cnt = 1

    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if graphs[j][i] == graphs[j-1][i]:
                cnt += 1
                if cnt > ans:
                    ans = cnt
            else:
                cnt = 1
    
    return ans


n = int(input())
graphs = [list(input()) for _ in range(n)]

ans = 1
for i in range(n):
    for j in range(n):
        if i < n-1:
            graphs[i][j], graphs[i+1][j] = graphs[i+1][j], graphs[i][j]
            ans = max(ans, cal_max_candy(graphs))
            graphs[i][j], graphs[i+1][j] = graphs[i+1][j], graphs[i][j]
        if j < n-1:
            graphs[i][j], graphs[i][j+1] = graphs[i][j+1], graphs[i][j]
            ans = max(ans, cal_max_candy(graphs))
            graphs[i][j], graphs[i][j+1] = graphs[i][j+1], graphs[i][j]
        
print(ans)
