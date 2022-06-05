# solved: [13904] 과제
# https://www.acmicpc.net/problem/13904
# greedy, sorting
# 
# Gold 3
# 먼저 w가 큰 순으로, d가 작은 순으로 정렬
# 위의 정렬한 순서대로 w를 days의 해당 날짜(d)에 기록
# 해당 날짜(d)가 차있으면, d보다 작으면서 최초로 비어있는 날짜 (find_idx(d))에 기록
# 모두 가득차있으면 pass
# days에 기록된 w의 합이 문제의 답

def find_idx(d):
    
    while d > 0:        
        if not days[d]:
            return d
        else:
            d -= 1
    else:
        return -1
    

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x:(x[1], -x[0]), reverse=True)
days = [0] * 1001

for d, w in arr:
    i = find_idx(d)
    if i == -1:
        continue
    else:
        days[i] = w
        
print(sum(days))
