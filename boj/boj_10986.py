# solved: [10986] 나머지 합
# https://www.acmicpc.net/problem/10986
# prefix-sum
# 
# Gold 3
# (a[i] + ... + a[j]) % m = 0 <=====> (a[1]+...+a[j]) % m = (a[1]+...+a[i-1]) % m
# 즉, m으로 나눈 두 개의 누적합을 선택하는 가짓 수
# psum_dict에 m으로 나눈 나머지를 갖는 누적합의 개수를 counting하여 최종 value에 대하여 vC2 개수의 합을 return

from collections import defaultdict

n, k = map(int, input().split())
nums = list(map(lambda x:int(x)%k, input().split()))

psum_dict = defaultdict(int)
temp = 0
for i in range(n):
    temp += nums[i]
    temp %= k
    psum_dict[temp] += 1

ans = 0
for k, v in psum_dict.items():
    if k == 0:
        ans += psum_dict[k]
    ans += v*(v-1)//2
print(ans)
