# solved: [2630] 색종이 만들기
# https://www.acmicpc.net/problem/2630
# divide-and-conquer, recursion
# 
# Silver 3
# 1. 각 색종이의 변을 4개의 색종이로 쪼갠 후
# 2. 색종이의 색이 모두 하나인지 체크 (set(sum(arr, [])))의 원소가 하나인지 체크)
# 3-1. 하나인 경우 그 색의 변수를 +1
# 3-2. 아닌 경우 1의 과정을 반복

def get(arr, x1, x2, y1, y2):
    
    return [[arr[x][y] for y in range(y1, y2)] for x in range(x1, x2)]

def dq(arr):
    
    global white, blue
    
    chk = set(sum(arr, []))
    
    if len(chk) == 1:
        if chk == {1}:
            blue += 1
        else:
            white += 1
    else:
        n = len(arr)
        m = n // 2
        dq(get(arr, 0, m, 0, m))
        dq(get(arr, 0, m, m, n))
        dq(get(arr, m, n, 0, m))
        dq(get(arr, m, n, m, n))


n = int(input())
papers = [list(map(int, input().split())) for _ in range(n)]

white, blue = 0, 0
dq(papers)

print(white, blue, sep='\n')
