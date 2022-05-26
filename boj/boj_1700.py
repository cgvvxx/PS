# solved: [1700] 멀티탭 스케줄링
# https://www.acmicpc.net/problem/1700
# greedy
# 
# Gold 1
# 현재 멀티탭 구멍 개수 만큼 plugged에 전기용품을 담고
# plugged가 꽉 찬 경우, plugged에 있는 전기용품 중 가장 마지막에 사용하는 (혹은 사용하지 않는) 전기용품을 pop하고 cnt += 1
# popped_app : 현재 가장 마지막에 사용하는 (혹은 사용하지 않는) 전기용품을 return 하는 함수
# 즉, greedy하게 현재 사용중인 전기용품 중 가장 마지막에 사용하는 전기용품을 플러그에서 제거하는 방식으로 진행

def popped_app(i, plugged):
    
    check = -1
    for p in plugged:
        try:
            j = apps[i:].index(p)
            if j > check:
                popped = p
                check = j
        except:
            return p
    
    return popped


N, K = map(int, input().split())
apps = list(map(int, input().split()))

plugged = set()
cnt = 0
for i in range(K):
    
    app = apps[i]
    
    if len(plugged) < N:
        plugged.add(app)
    else:
        if app not in plugged:
            popped = popped_app(i, plugged)
            plugged.remove(popped)
            plugged.add(app)
            cnt += 1

print(cnt)  
