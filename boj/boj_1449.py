# solved: [1449] 수리공 항승
# https://www.acmicpc.net/problem/1449
# greedy, sorting
# 
# Silver 3
# 물이 새는 곳의 위치를 담은 leaks를 정렬
# leaks의 각 원소(물이 새는 곳의 위치)를 순회하면서 다음 테이프의 위치(nxt)에 대해
# n > nxt인 경우 nxt = n + L - 1로 업데이트하고 테이프의 개수(ans)는 +1
# 시간복잡도는 leaks의 정렬로 O(nlogn)

N, L = map(int, input().split())
leaks = list(map(int, input().split()))

leaks.sort()

ans = 0
nxt = -1
for n in leaks:
    if n > nxt:
        nxt = n + L - 1
        ans += 1
        
print(ans)
