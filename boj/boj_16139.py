# solved: [16139] 인간-컴퓨터 상호작용
# https://www.acmicpc.net/problem/16139
# prefix-sum
# 
# Silver 2
# 누적 합 기본 문제 + 단어를 숫자로 치환

import sys
input = sys.stdin.readline

s = input().strip()

psum = [[0] * (len(s)+1) for _ in range(26)]
for i in range(26):
    for j in range(len(s)):
        if ord(s[j]) - 97 == i:
            psum[i][j+1] = psum[i][j] + 1
        else:
            psum[i][j+1] = psum[i][j]

for _ in range(int(input().strip())):
    a, l, r = input().split()
    idx = ord(a) - 97
    print(psum[idx][int(r)+1]-psum[idx][int(l)])
