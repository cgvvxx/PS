# Programmers - 조이스틱
# Level 2
# 그리디

def rot_from_A(s): # 위 또는 아래로 돌릴 때 주어진 글자까지 최소로 움직이는 횟수
    return min(ord(s) - ord('A'), ord('Z') - ord(s) + 1)


def transverse(name): # 방향 전환 없는 경우의 조이스틱 조작횟수
    if name == 'A' * len(name):
        return 0

    count = -1
    count_A = []
    for char in name:
        count += 1
        if char == 'A':
            count_A.append(char)
        else:
            count_A = []
            count += rot_from_A(char)

    return count - len(count_A)


def solution(name):
    right_A_idx = name[1:].find('A') + 2
    left_A_idx = name[1:].rfind('A') + 2
    answer = []

    answer.append(transverse(name)) # 기존 방향(오른쪽)대로의 조이스틱 조작횟수
    answer.append(transverse(name[0] + name[1:][::-1])) # 왼쪽 방향으로의 조이스틱 조작횟수

    if right_A_idx != 1 and left_A_idx != 1:
        answer.append(transverse(name[:right_A_idx]) # 기존 방향으로의 조작 후 'A' 글자를 만나면 방향을 바꾸는 경우의 조작횟수
                      + right_A_idx - 1 + transverse(name[right_A_idx:][::-1]))
        answer.append(transverse(name[0] + name[left_A_idx:][::-1]) # 위와 반대의 경우
                      + len(name) - left_A_idx + 1 + transverse(name[1:left_A_idx - 1]))

    return min(answer)