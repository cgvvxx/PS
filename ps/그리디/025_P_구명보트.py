# Programmers - 구명보트
# Level 2
# 그리디

def solution(people, limit):
    people.sort(reverse=True)  # people 내림차순 정렬
    answer = 0
    right = len(people) - 1

    for left in range(len(people)):  # 왼쪽부터 카운팅
        if left > right:
            return answer
        if people[left] + people[right] <= limit:  # 가장 큰 무게와 작은 무게의 합이 limit 보다 작으면 카운팅
            right -= 1
        answer += 1

    return answer