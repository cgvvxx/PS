# solved: [1992] 쿼드트리
# https://www.acmicpc.net/problem/1992
# divide-and-conquer, recursion
# 
# Silver 1
# boj 2630과 비슷한 문제
# 이 때 return 값은, 주어진 배열에 유일한 문자이고 4개로 쪼개진 경우는 앞뒤로 "("와 ")"를 추가해야 함

def get(arr, x1, x2, y1, y2):
    
    return [[arr[x][y] for y in range(y1, y2)] for x in range(x1, x2)]

def dq(arr):
    
    ans = "("
    
    chk = set(sum(arr, []))
    
    if len(chk) == 1:
        return chk.pop()
    else:
        n = len(arr)
        m = n // 2
        for i in range(2):
            for j in range(2):
                ans += dq(get(arr, i*m, (i+1)*m, j*m, (j+1)*m))
        ans += ")"
        return ans


n = int(input())
images = [list(input()) for _ in range(n)]

print(dq(images))
