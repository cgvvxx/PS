# Baekjoon 20164 - 홀수 홀릭 호석
# Gold 5


def count_odds(num: str):
    
    ans = 0
    for i in num:
        i = int(i)
        if i % 2 == 1:
            ans += 1
    
    return ans


def sum_digit(num: str):
    
    ans = 0
    for i in num:
        ans += int(i)
        
    return str(ans)


def division(num: str):
    
    if len(num) == 1:
        
        c = count_odds(num)
        return [c, c]
    
    elif len(num) == 2 or len(num) == 3:
        
        c = count_odds(num)
        d1, d2 = division(sum_digit(num))
        
        return [c + d1, c + d2]
    
    else:
        
        l = len(num)
        mmin = 10000
        mmax = -1
        c = count_odds(num)
        
        for i in range(1, l):
            for j in range(i+1, l):
                
                d1, d2 = division(str(int(num[:i])+int(num[i:j])+int(num[j:])))
                
                mmin = min(mmin, d1)
                mmax = max(mmax, d2)
                
        return [c + mmin, c + mmax]
    
    
print(*division((input())))


# count_odds ; 주어진 숫자에서 홀수 개수의 합
# sum_digit ; 주어진 숫자에서 모든 숫자의 합
# division ; 재귀적으로 구현, 리턴 값은 [최솟값, 최댓값]
# 한 자리 숫자일 때, 그 숫자가 홀수이면 [1, 1] 짝수이면 [0, 0]
# 두 자리 숫자일 때, 
# division(모든 숫자의 합) + 홀수 개수의 합
# 세 자리 이상 숫자일 때, 세 자리 숫자를 모두 쪼개는 경우의 수를 돌린 후
# [최솟값 + 홀수 개수의 합, 최댓값 + 홀수 개수의 합]