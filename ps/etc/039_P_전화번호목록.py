# Programmers - 전화번호 목록
# Level 2
# 해시

def solution(phone_book):
    phone_book.sort()

    for idx in range(len(phone_book)):
        if idx == len(phone_book) - 1:
            return True
        else:
            if phone_book[idx] == phone_book[idx + 1][:len(phone_book[idx])]:
                return False