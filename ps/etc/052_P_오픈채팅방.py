# Programmers - 오픈채팅방
# Level 2

def change_word(answer, user_dict):
    result = []
    for ans in answer:
        if ans[1] == 'E':
            result.append(f"{user_dict[ans[0]]}님이 들어왔습니다.")
        else:
            result.append(f"{user_dict[ans[0]]}님이 나갔습니다.")

    return result


def solution(record):
    user_dict = dict()
    answer = []
    for rec in record:

        rec_splited = rec.split()
        if rec[0] == 'C':
            user_dict[rec_splited[1]] = rec_splited[2]
        else:
            is_enter = rec[0]
            answer.append((rec_splited[1], is_enter))
            if is_enter == 'E':
                user_dict[rec_splited[1]] = rec_splited[2]

    return change_word(answer, user_dict)