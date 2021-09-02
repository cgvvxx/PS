# Baekjoon 15886 - 내 선물을 받아줘2
# Silver 1


n = int(input())
route = input()

ans = 0
opened = False
for i in route:
    if i == 'E' and not opened:
        opened = True
        continue
        
    if i == 'W' and opened:
        opened = False
        ans += 1
        continue

print(ans)    


# E와 W로 이루어진 구간을 counting 하는 문제
# 앞에서 부터 순회하면서 E와 opened, W와 opened를 체크해서 ans에 1씩 counting
# 시간복잡도 O(n)