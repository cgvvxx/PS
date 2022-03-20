# solved: [1806] 부분합
# https://www.acmicpc.net/problem/1806
# two-pointer
# 
# Gold 4
# 기본적으로 l, r 투 포인터를 이용하여 l과 r 사이의 배열의 합을 구하고
# 그 합이 s보다 크면 l += 1, 아니면 r += 1, r이 끝에 도달하면 break
# 이 때, 인덱스를 이용하므로 더하는 순서 주의

n, s = map(int, input().split())
arr = list(map(int, input().split()))

l, r = 0, 0
ans = 10**5
check = 0

while True:
    
    if check >= s:
        ans = min(ans, r-l)
        check -= arr[l]
        l += 1
    elif r >= n:
        break
    else:
        check += arr[r]
        r += 1

if ans >= 10**5:
    print(0)
else:
    print(ans)
