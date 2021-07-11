# Programmers - 디스크 컨트롤러
# Level 3
# 스택/큐 - 힙

def condition_sort(jobs, t):
    under_t = []
    over_t = []
    for job in jobs:
        if job[0] <= t:
            under_t.append(job)
        else:
            over_t.append(job)

    under_t.sort(key=lambda x: x[1])
    over_t.sort(key=lambda x: (x[0], x[1]))

    return under_t + over_t


def solution(jobs):
    jobs_len = len(jobs)
    ans = 0

    jobs.sort(key=lambda x: (x[0], x[1]))  # jobs의 시작 시간을 기준으로 정렬
    t = jobs[0][0]  # jobs의 시작 시간이 가장 빠른 시간이 시작 시각

    while jobs:
        ele = jobs.pop(0)
        if t >= ele[0]:  # 현재 시각보다 jobs의 시작 시간이 빠른경우
            ans += (t + ele[1] - ele[0])
            t += ele[1]
        else:  # 현재 시각보다 jobs의 시작 시간이 빠른 경우가 없는 경우
            ans += ele[1]
            t = ele[0] + ele[1]

        jobs = condition_sort(jobs, t)
    # jobs에서 시작 시간이 t보다 작은 경우와 t보다 큰 경우를 나눠서 sort

    return ans // jobs_len