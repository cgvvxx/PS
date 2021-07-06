# Programmers - 베스트앨범
# Level 3
# 해시

def sum_second(list):
    list_sum = 0
    for i, j in list:
        list_sum += j

    return list_sum


def solution(genres, plays):
    song_dict = dict()

    for i in range(len(genres)):
        try:
            song_dict[genres[i]].append((i, plays[i]))
        except:
            song_dict[genres[i]] = [(i, plays[i])]

    high = [(idx, sum_second(val)) for idx, val in enumerate(song_dict.values())]
    high.sort(key=lambda x: x[1], reverse=True)

    ans = []
    dict_keys = list(song_dict.keys())

    for i in range(len(song_dict)):
        cat_list = song_dict[dict_keys[high[i][0]]]
        if len(cat_list) == 1:
            ans.append(cat_list[0][0])
        else:
            cat_list.sort(key=lambda x: x[1], reverse=True)
            ans.append(cat_list[0][0])
            ans.append(cat_list[1][0])

    return ans