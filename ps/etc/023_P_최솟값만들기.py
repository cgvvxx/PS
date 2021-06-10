# Programmers - 최솟값 만들기
# Level 2

def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    answer = 0

    for i, j in zip(A, B):
        answer += i * j

    return answer