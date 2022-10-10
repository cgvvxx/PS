# solved: [20920] 영단어 암기는 괴로워
# https://www.acmicpc.net/problem/20920
# sorting
# 
# Silver 3
# 단순히 Counter를 이용해서 문제의 조건에 맞게 정렬

from collections import Counter
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
words = []
for _ in range(n):
    word = input().strip()
    if len(word) < m:
        continue
    words.append(word)
    
c = Counter(words)
for item in sorted(list(c.items()), key=lambda x:(-x[1], -len(x[0]), x[0])):
    print(item[0])
