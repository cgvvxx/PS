# Baekjoon 2636 - 치즈
# Gold 5
# BFS/DFS


def dfs(x, y):
    
    global count    
    visited[x][y] = True
    
    for i in range(4):
        
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
            
        if visited[nx][ny]:
            continue
            
        visited[nx][ny] = True
        
        if arr[nx][ny] == 1:
            arr[nx][ny] = 0
            count += 1
            continue
        
        if arr[nx][ny] == 0:
            dfs(nx, ny)
            
    return count


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

times = []
answer = []
while True:
    
    count = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    answer.append(dfs(0, 0))
    times.append(1)
    
    if answer[-1] == 0:
        break

print(sum(times[:-1]))
print(answer[-2])

# 처음에는 bfs로 (0, 0)에서 시작하여 바깥 공기 부분을 -1로 설정 후 다시 치즈를 돌면서 주위가 음수인 부분을 제거
# 16%에서 틀렸다고 나오는데 도저히 반례를 찾을 수 없음.. 반례 찾느라 한시간 이상 걸린듯
# 아예 dfs로 풀이를 바꾸니 성공
# (0, 0)에서 시작해서 dfs로 방문체크를 하면서 돌아다니고, 1(치즈)을 만날때만 0으로 바꿈
# 일단 재귀함수로 풀고 재귀 깊이 설정을 했는데 다음엔 스택으로 해보는 것도 좋을듯