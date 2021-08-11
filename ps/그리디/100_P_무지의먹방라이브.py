# Programmers - 무지의 먹방 라이브
# Level 4
# 그리디


def solution(food_times, k):

    foods = [[idx, food_time] for idx, food_time in enumerate(food_times)]
    foods.sort(key=lambda x:(x[1], x[0]))
    len_food = len(foods)

    before_del_num = 0
    for i in range(len(foods)):

        del_num = foods[i][1]
        this_term = len_food * (del_num - before_del_num)
        
        if k >= this_term:
            k -= this_term
            before_del_num = del_num
            len_food -= 1
        else:    
            break
    else:
        return -1
    
    new_foods = foods[i:]
    new_foods.sort()
    
    return new_foods[k % len(new_foods)][0] + 1