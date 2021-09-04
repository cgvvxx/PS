# Baekjoon 8980 - 택배
# Gold 3
# 그리디


sends = []
n, c = map(int, input().split())
for _ in range(int(input())):
    i, j, k = map(int, input().split())
    sends.append((i, j, k))
    
sends.sort(key=lambda x:x[1])
trucks = [0] * (n+1)
total = 0

for _from, _to, burden in sends:

    left = min(c - max(trucks[_from:_to]), burden)
    if left > 0:
        total += left
        for i in range(_from, _to):
            trucks[i] += left

print(total)


# 처음엔 시작 지점을 기준으로 차례대로 앞에서부터 배달해나가면서 했었는데 X
# 가장 짐을 먼저 내릴수 있는 도착지점으로 정렬 후 배달해나감