# solved: [1987] 알파벳
# https://www.acmicpc.net/problem/1987
# backtracking, dfs, graph-traversal
# 
# Gold 4
# 단순히 dfs를 통해 현재까지 거쳐온 루트(trace)를 체크하면서 현재 탐색하는 노드의 값이 trace에 없는 경우만 진행
# (*) 이 때 visited[nx][ny]에 현재까지의 루트(trace)를 기록하여 다시 되돌아 가지 않도록 가지치기하는게 중요
# (*) 없이 진행하면 최악의 케이스에 8초를 통과하여 무조건 시간초과! (2x1, ex2 반례 체크)
# (*) 조건 추가시 pypy3로 약 320ms로 통과
# ex1.
# 20 20
# YACDEFBXZJKVAXZXBSVA
# BCDEFGHIJKLMNSVUTBSV
# CDEFGHIJKLMNORTXUTBS
# DEFGHIJKLMNOPQWZXUTW
# AFGHIJKLMNOPQRSVZXWT
# XGHIJKLMNOPQRSTBXZVU
# WHIJKLMNOPQRSTUVWXZZ
# HIJKLMNOPQRSTUVZXWZA
# IJKLMNOPQRSTUVWXZZAB
# JKLMNOPQRSTUVZXWZABC
# TLMNOPQRSTUVWXWZABCD
# QZNOPQRSTUVZXZZABCDE
# ZRSPQRSTUVZXWZABCDEF
# AVUXTSTUVZXWZABCDEFG
# ZBWUAWXVWXWZABCDEFGH
# ZRVWVUWAXZZABCDEFGHI
# SRZVZVAXZZABCDEFGHIJ
# TSRZSBUZZABCDEFGHIJK
# QTSRTXZZABCDEFGHIJKL
# CQTQQZZABCDEFGHIJKLM
# ex2.
# 20 20
# YBCDEFGHUJZAQFOJRQXH
# HAXNLTWMSKIVAPNOJZQD
# PMCOSPIJQPREGQZPFLRU
# VDGIWVDFHUAHFKUJHAOX
# TQKLUZPLRQOQUVIDJOZI
# ZFRJRTTHUGTJNIXKGUBC
# UHPASLMQZAMRIKQJOEZA
# MTZHFKJGJKQJKZWOAZAA
# VUTGSVFQRITNFSBCEAAB
# MWDQFTAKDFMGIOCEAABC
# SQVFEQXRBAUPRMEAABCD
# FGWUVWKIAENSCEAABCDE
# KVSXEZXDENBHAAABCDEF
# SEEJSKPENBPAAABCDEFG
# NFUAWDUCHPFAABCDEFGH
# SMLFVTRMHGAABCDEFGHI
# HNINXFMFEAABCDEFGHIJ
# FMJQJOGEAABCDEFGHIJK
# QFOFOFEAABCDEFGHIJKL
# AHFOAAAABCDEFGHIJKLM


import sys
input = sys.stdin.readline


def dfs(x, y, trace, cnt):
    
    global ans, flag

    ans = max(ans, cnt)
    
    if ans >= min(26, r*c):
        flag = True
        return

    for i in range(4):
        
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue
        
        if graphs[nx][ny] in trace:
            continue

        if visited[nx][ny] != trace + graphs[nx][ny]:
            visited[nx][ny] = trace + graphs[nx][ny]
            dfs(nx, ny, trace + graphs[nx][ny], cnt+1)
        
            if flag:
                return 


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

r, c = map(int, input().split())
graphs = [list(input()) for _ in range(r)]
visited = [[''] * c for _ in range(r)]

ans = 0
flag = False

dfs(0, 0, graphs[0][0], 1)
print(ans)
