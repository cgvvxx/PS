# Baekjoon 2503 - 숫자 야구
# Silver 4
# 완전탐색


from itertools import permutations\


def get_yagu(num1: int, num2: int):
    
    num1 = str(num1)
    num2 = str(num2)
    
    s = 0
    b = len(set(list(num1)) & set(list(num2)))
    
    for i in range(3):
        if num1[i] == num2[i]:
            s += 1
            
    b -= s
    
    return s, b


n = int(input())
nums = []
sb = []
for _ in range(n):
    
    num, s, b = map(int, input().split())
    nums.append(num)
    sb.append((s, b))
    
ans = 0
for comb in permutations('123456789', 3):
    
    check_num = ''.join(comb)
    for i in range(n):
        s, b = get_yagu(nums[i], check_num)
        if (s, b) != sb[i]:
            break
    else:
        ans += 1

print(ans)


# 서로 다른 1~9 숫자로 이루어진 세 자리 정수의 개수는 9*8*7으로 매우 작으므로
# permutations을 통한 완전탐색