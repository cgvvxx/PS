# Baekjoon 22860 - 폴더 정리(small)
# Gold 3
# BFS/DFS


from collections import defaultdict


def dfs(p):
    
    stack = [p]
    my_files = []
    visited = set()
    
    while stack:
        
        p = stack.pop()
        
        if p in files:
            my_files.extend(files[p])
        
        if p in folders and p not in visited:
            visited.add(p)
            stack.extend(folders[p])
            
    return my_files


def get_files(my_files):
    
    print(len(set(my_files)), len(my_files))
    
    

folders = defaultdict(list)
files = defaultdict(list)
n, m = map(int, input().split())

for _ in range(n+m):
    p, f, c = input().split()
    
    if c == '1':
        folders[p].append(f)
    else:
        files[p].append(f)

        
for _ in range(int(input())):
    
    s = input()
    if s == 'main':
        get_files(dfs(s))
    else:
        get_files(dfs(s.split('/')[-1]))


# 폴더인지 파일인지 구분하여 folders / files dict에 append
# 폴더가 주어질 때마다 dfs를 통해 하위 폴더들의 파일을 리스트에 모두 담아서 return
# 모든 파일의 개수 = 리스트의 길이
# 서로 다른 파일의 개수 = set(list)의 길이