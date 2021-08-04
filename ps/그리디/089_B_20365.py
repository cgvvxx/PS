# Baekjoon 20365 - 블로그 2
# Silver 2
# 그리디

n = int(input())
colors = input()

new_colors = colors[0] 
# new_color는 colors에서 색이 바뀌는 경우만 append
# ex) colors = 'RRBBRRRBR' > new_colors = 'RBRBR'

for color in colors:
    if new_colors[-1] != color:
        new_colors += color
        
b = new_colors.count('B')
r = new_colors.count('R')

print(min(b,r) + 1) # 색깔이 바뀌는 지점의 최솟값 + 1