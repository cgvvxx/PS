# solved: [1074] Z
# https://www.acmicpc.net/problem/1074
# divide-and-conquer, recursion
# 
# Silver 1
# 분할 정복을 통해 현재 위치 (r, c)까지 찾아가는 문제
# x, y는 해당 사각형의 시작 점(좌상단), d는 해당 사각형의 가로 길이
# 좌상단, 우상단, 좌하단, 우하단을 방문하면서 현재 r, c가 해당 사각형에 있는지 체크
# 없는 경우 그 사각형의 크기 만큼 ans에 더하고, 있는 경우 지금까지 더해진 ans를 print

def dq(x, y, d):
    
    global ans
    
    if (x, y) == (r, c):
        print(ans)
        return
    
    if d == 1:
        ans += d
        return
    
    if r < x or r >= x+d or c < y or c >= y+d:
        ans += d**2
        return
    
    m = d//2
    dq(x, y, m)
    dq(x, y+m, m)
    dq(x+m, y, m)
    dq(x+m, y+m, m)


n, r, c = map(int, input().split())
ans = 0
dq(0, 0, 2**n)    
