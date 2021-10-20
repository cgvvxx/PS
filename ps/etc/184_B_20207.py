# Baekjoon 20207 - 달력
# Silver 1
# 구현


schedules = []
for _ in range(int(input())):
    schedules.append(tuple(map(int, input().split())))
schedules.sort(key=lambda x:(x[0], -x[1]))

ans = 0
start = -1
end = -1
flag = False
cnt = []
for s, e in schedules:

    if not cnt:
        cnt.append(e)
        start = s
        end = e
        continue
    
    for idx in range(len(cnt)):
        
        if cnt[idx] < s:
            if end + 1 < s:
                ans += (max(cnt) - start + 1) * len(cnt)
                cnt = [e]
                start = s
                end = e
            else:
                cnt[idx] = e
                end = max(end, e)
            break
        
    else:
        cnt.append(e)
        end = max(end, e)

ans += (max(cnt) - start + 1) * len(cnt)

print(ans)


# 정렬? 구현? 문제
# 달력의 끝나는 날짜를 카운팅하는 cnt라는 리스트를 만든 뒤 문제의 조건에 맞게 cnt에 끝나는 날짜를 업데이트해나감
# 문제를 풀면서 계속 틀렸는데 문제의 예제를 제외한 반례를 찾는 것이 너무 어려웠음..
# 반례1) 앞에서부터 cnt를 체크하나가는데 뒤의 원소보다 앞의 원소의 끝나는 길이가 짧은 케이스
# 3
# 1 4
# 4 8
# 8 9
# 반례2) 하루 차이로 이어붙여진 계획은 하나의 직사각형으로 계산하여야함
# 3
# 1 2
# 2 3
# 4 5