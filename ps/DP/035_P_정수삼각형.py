# Programmers - 정수 삼각형
# Level 3
# DP

def solution(triangle):
    count = triangle[:]  # 각 root의 최댓값을 count하는 배열 복사
    for i in range(len(triangle)):
        for j in range(i + 1):
            if i == 0:
                continue
            if j == 0:
                count[i][j] += count[i - 1][j]
            elif j == i:
                count[i][j] += count[i - 1][j - 1]
            else:  # triangle의 i,j 원소는 (i-1,j-1), (i-1, j)의 최댓값에 (i, j) 원소를 더한 값
                count[i][j] += max(count[i - 1][j - 1], count[i - 1][j])

    return max(count[-1])