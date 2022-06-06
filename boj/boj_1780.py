# solved: [1780] 종이의 개수
# https://www.acmicpc.net/problem/1780
# divide-and-conquer, recursion
# 
# Silver 2
# boj 2630과 비슷한 문제
# 단, n이 2의 거듭제곱이 아닌 3의 거듭제곱의 꼴로 주어짐

def get(arr, x1, x2, y1, y2):
    
    return [[arr[x][y] for y in range(y1, y2)] for x in range(x1, x2)]


def dq(arr):
    
    global ans1, ans2, ans3
    
    chk = set(sum(arr, []))
    
    if len(chk) == 1:
        if chk == {-1}:
            ans1 += 1
        elif chk == {0}:
            ans2 += 1
        else:
            ans3 += 1
    else:
        n = len(arr)
        m = n // 3
        for i in range(3):
            for j in range(3):
                dq(get(arr, i*m, (i+1)*m, j*m, (j+1)*m))


n = int(input())
papers = [list(map(int, input().split())) for _ in range(n)]

ans1, ans2, ans3 = 0, 0, 0
dq(papers)

print(ans1, ans2, ans3, sep='\n')
