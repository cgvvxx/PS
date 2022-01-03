# Baekjoon 15779 - Zigzag
# Silver 5


n = int(input())
arrs = list(map(int, input().split()))

start = False
up = None
idx = 0
cnt = 1
ans = 1

while idx < n-1:
    
    idx += 1
    
    if not start:
        start = True
        
        if arrs[idx-1] < arrs[idx]:
            up = True
        elif arrs[idx-1] > arrs[idx]:
            up = False
        else:
            start = False
    else:
        if up and arrs[idx-1] > arrs[idx]:
            up = False
            cnt += 1
        elif not up and arrs[idx-1] < arrs[idx]:
            up = True
            cnt += 1
        else:
            up = None
            start = False
            cnt = 1
            idx -= 1
            
        ans = max(ans, cnt)

print(ans+1)
    

# 지그재그 수열을 찾는 단순 구현
# idx = 0 부터 시작하여 배열의 숫자들을 돌면서 크기가 커지고 작아지고가 반복함을 체크