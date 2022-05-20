# solved: [2217] 로프
# https://www.acmicpc.net/problem/2217
# greedy, sorting
# 
# Silver 4
# 로프의 길이 순으로 정렬 > (길이) * (그 길이보다 긴 로프의 개수) 의 최댓값
# 이 경우 시간복잡도는 O(nlogn) (정렬)
# 문제에서 로프의 길이의 최댓값이 10000으로 정해져있으므로 로프의 길이에 해당하는 개수를 카운팅하는 길이가 10000인 리스트 할당 후
# 최댓값을 찾으면 시간복잡도 O(n)까지 줄일 수 있음

n = int(input())
ropes = [int(input()) for _ in range(n)]

ropes.sort()
ans = 0
for i, r in enumerate(ropes):
    ans = max(ans, r*(n-i))
print(ans)
