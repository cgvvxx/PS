# Programmers - 파일명 정렬
# Level 2
# 정렬


def get_head_num(file):
    
    num = ''
    is_num = False
    num_idx = 0
    
    for idx, char in enumerate(file):
        if char.isdigit():
            if not is_num:
                num_idx = idx
            num += char
            is_num = True
        else:
            if is_num:
                break
    
    return file[:num_idx].lower(), int(num)

def solution(files):
    
    files.sort(key=get_head_num)
    
    return files