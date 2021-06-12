# Programmers - H-index
# Level 2
# 정렬

def solution(citations):
    citations.sort()
    answer = len(citations) + 1

    while True:  # 전체 길이부터 시작하여 1씩 빼면서 h-index 조건 만족하는지 체크

        answer -= 1
        if sum([i >= answer for i in citations]) >= answer:
            break

    return answer
