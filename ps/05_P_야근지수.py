# Programmers - 야근지수

def over_night(works, n):
    answer = 0
    if n >= sum(works):
        return answer
    else:
        works.sort(reverse=True)
        while n > 0:
            for i in range(len(works)):
                works[i] -= 1
                n -= 1

                if n == 0:
                    for i in works:
                        answer += i**2
                    return answer

                if works[i] >= works[i+1]:
                    break